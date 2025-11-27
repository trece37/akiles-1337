"""
Configuración centralizada del proyecto Akiles-1337
Gestiona parámetros de trading, modelos y conexiones
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# ==================== CONFIGURACIÓN MT5 ====================
MT5_SYMBOL = "EURUSD"
MT5_TIMEFRAME = 60  # 1 hora en minutos
MT5_LOOKBACK_DAYS = 365  # Datos históricos
MT5_ACCOUNT = os.getenv("MT5_ACCOUNT", "")
MT5_PASSWORD = os.getenv("MT5_PASSWORD", "")
MT5_SERVER = os.getenv("MT5_SERVER", "")

# ==================== CONFIGURACIÓN LSTM ====================
LSTM_SEQUENCE_LENGTH = 60  # Ventana temporal (barras)
LSTM_FEATURES = 11  # RSI, EMA20, EMA50, ATR, MACD, Bollinger, Vol, etc
LSTM_UNITS = [128, 64, 32]  # Capas LSTM
LSTM_DROPOUT = 0.2
LSTM_BATCH_SIZE = 32
LSTM_EPOCHS = 50
LSTM_VALIDATION_SPLIT = 0.2

# ==================== FEATURE ENGINEERING ====================
RSI_PERIOD = 14
EMA_FAST = 20
EMA_SLOW = 50
ATR_PERIOD = 14
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
BOLLINGER_PERIOD = 20
BOLLINGER_STD = 2

# ==================== TRADING ====================
LOT_SIZE = 0.1
STOP_LOSS_PIPS = 50
TAKE_PROFIT_PIPS = 150
MAX_OPEN_POSITIONS = 3
MIN_CONFIDENCE = 0.65  # Umbral de predicción

# ==================== GOOGLE CLOUD ====================
GCP_PROJECT = os.getenv("GCP_PROJECT", "")
GCP_REGION = "us-central1"
VERTEX_AI_ENDPOINT = os.getenv("VERTEX_AI_ENDPOINT", "")
MODEL_NAME = "akiles-lstm-v3.1"
BUCKET_NAME = os.getenv("GCS_BUCKET", "akiles-models")

# ==================== LOGGING ====================
LOG_LEVEL = "INFO"
LOG_FILE = "logs/akiles.log"
