# EN: akiles-1337/src/predictor.py

import os
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Layer
from tensorflow.keras import backend as K

# ==============================================================================
# 1. DEFINICIÓN DE LA CAPA DE ATENCIÓN (AttentionLayer)
# CRÍTICO: Debe ser IDÉNTICA a la usada en el Notebook de entrenamiento.
# Si no está aquí, Vertex AI no podrá cargar el modelo guardado.
# ==============================================================================
class AttentionLayer(Layer):
    def __init__(self, **kwargs):
        super(AttentionLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        feature_dim = input_shape[-1]
        self.W = self.add_weight(name='attention_weight',
                                 shape=(feature_dim, feature_dim),
                                 initializer='glorot_uniform',
                                 trainable=True)
        self.b = self.add_weight(name='attention_bias',
                                 shape=(feature_dim,),
                                 initializer='zeros',
                                 trainable=True)
        self.u = self.add_weight(name='attention_vector',
                                 shape=(feature_dim,),
                                 initializer='glorot_uniform',
                                 trainable=True)
        super(AttentionLayer, self).build(input_shape)

    def call(self, inputs):
        score = K.tanh(K.dot(inputs, self.W) + self.b)
        attention_weights = K.softmax(K.dot(score, self.u), axis=1)
        context_vector = attention_weights * inputs
        context_vector = K.sum(context_vector, axis=1)
        return context_vector

    def get_config(self):
        config = super(AttentionLayer, self).get_config()
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)

# ==============================================================================
# 2. CLASE PREDICTOR (El cerebro del despliegue)
# ==============================================================================
class MyPredictor(object):
    def __init__(self, model_burocrata, scaler_burocrata, model_seldon, scaler_seldon):
        self._model_burocrata = model_burocrata
        self._scaler_burocrata = scaler_burocrata
        self._model_seldon = model_seldon
        self._scaler_seldon = scaler_seldon
        self._num_features_burocrata = scaler_burocrata.n_features_in_
        self._num_features_seldon = scaler_seldon.n_features_in_

    def _get_regime(self, instances):
        """
        AGENTE GUARDIÁN (Simple): Decide qué modelo usar.
        Aquí usamos el VIX como detector. Asumimos que VIX es la feature índice 10.
        """
        # instances shape (1, 60, 12)
        vix_actual = instances[0][-1][10] # VIX de la última vela
        VIX_CRISIS_THRESHOLD = 30.0
        
        if vix_actual > VIX_CRISIS_THRESHOLD:
            return "CRISIS"
        else:
            return "NORMAL"

    def predict(self, instances, **kwargs):
        """
        Lógica de inferencia del MoE.
        1. Recibe datos CRUDOS.
        2. El Agente Guardián decide el régimen.
        3. Escala, Predice, Devuelve probabilidades.
        """
        try:
            inputs_raw = np.asarray(instances, dtype=np.float32)
            
            # 1. AGENTE GUARDIÁN
            regime = self._get_regime(inputs_raw)
            
            if regime == "CRISIS":
                model = self._model_seldon
                scaler = self._scaler_seldon
                num_features = self._num_features_seldon
            else:
                model = self._model_burocrata
                scaler = self._scaler_burocrata
                num_features = self._num_features_burocrata

            # 2. PRE-PROCESAMIENTO (Escalado)
            original_shape = inputs_raw.shape
            inputs_flattened = inputs_raw.reshape(-1, num_features)
            inputs_scaled = scaler.transform(inputs_flattened)
            inputs_scaled_3d = inputs_scaled.reshape(original_shape)

            # 3. INFERENCIA
            # Devuelve probabilidades [Prob_Venta, Prob_Lateral, Prob_Compra]
            probabilities = model.predict(inputs_scaled_3d)
            
            return probabilities.tolist()

        except Exception as e:
            return {"error": str(e)}

    @classmethod
    def from_path(cls, model_dir):
        """
        Carga TODOS los artefactos (los 2 modelos y los 2 scalers).
        """
        # Cargar Modelos (con la capa personalizada)
        model_burocrata = tf.keras.models.load_model(
            os.path.join(model_dir, 'model_burocrata.keras'), 
            custom_objects={'AttentionLayer': AttentionLayer}
        )
        model_seldon = tf.keras.models.load_model(
            os.path.join(model_dir, 'model_seldon.keras'), 
            custom_objects={'AttentionLayer': AttentionLayer}
        )

        # Cargar Scalers
        with open(os.path.join(model_dir, 'scaler_burocrata.pkl'), 'rb') as f:
            scaler_burocrata = pickle.load(f)
        with open(os.path.join(model_dir, 'scaler_seldon.pkl'), 'rb') as f:
            scaler_seldon = pickle.load(f)

        return cls(model_burocrata, scaler_burocrata, model_seldon, scaler_seldon)
