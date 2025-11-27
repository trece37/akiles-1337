"""
Utilidades generales para el proyecto Akiles
Funciones auxiliares de logging, validación y transformación de datos
"""

import logging
import os
from datetime import datetime
from src import config

# Configurar logging
def setup_logger(name: str) -> logging.Logger:
    """
    Configura un logger con formato estándar
    
    Args:
        name: Nombre del logger (típicamente __name__)
    
    Returns:
        Logger configurado
    """
    logger = logging.getLogger(name)
    logger.setLevel(config.LOG_LEVEL)
    
    # Crear carpeta de logs si no existe
    os.makedirs(os.path.dirname(config.LOG_FILE), exist_ok=True)
    
    # Handler a archivo
    fh = logging.FileHandler(config.LOG_FILE)
    fh.setLevel(config.LOG_LEVEL)
    
    # Formato
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    fh.setFormatter(formatter)
    
    logger.addHandler(fh)
    return logger


def validate_symbol(symbol: str) -> bool:
    """Valida que el símbolo sea válido"""
    return isinstance(symbol, str) and len(symbol) > 0


def timestamp_now() -> str:
    """Retorna timestamp actual en formato ISO"""
    return datetime.utcnow().isoformat()
