```ascii
   ___   __ __ ____  __    ____  ____       __ _____ _____ ______ 
  / _ | / //_//  _/ / /   / __/ / __/_____ <  /|_  /|_  //_  __/ 
 / __ |/ ,<  _/ /  / /__ / _/  _\ \/_____// /_ /_ <_/_ <  / /    
/_/ |_/_/|_|/___/ /____//___/ /___/     /_/(_)____/____/ /_/     
```

<div align="center">

### 🎯 ALGORITHMIC MARKET EXPLOITATION FRAMEWORK 🎯

**[ XAU/USD PREDICTION ENGINE • LSTM NEURAL WARFARE • MT5 EXECUTION ]**

![Python](https://img.shields.io/badge/Python_3.9+-14354C?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow_2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![GCP](https://img.shields.io/badge/Vertex_AI-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![MT5](https://img.shields.io/badge/MetaTrader_5-1C75BC?style=for-the-badge&logo=metaquotes&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-SANDBOX_MODE-yellow?style=for-the-badge)

*«We don't predict markets, we calculate probabilities»*

</div>

---

## 📡 MISSION OVERVIEW

**AKILES-1337** es un sistema híbrido de trading algorítmico que combina:
- 🧠 **CEREBRO**: Deep Learning en Google Vertex AI
- ⚡ **OBRERO**: Ejecución ultrarrápida en MetaTrader 5
- 🎲 **TARGET**: XAU/USD (Gold) markets

### Hybrid Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   ☁️ CLOUD BRAIN                        │
│  ╔═══════════════════════════════════════════════════╗  │
│  ║  VERTEX AI • LSTM MODELS • PREDICTION ENGINE     ║  │
│  ║  • Feature Engineering                            ║  │
│  ║  • Multi-timeframe Analysis                       ║  │
│  ║  • Risk Calculation                               ║  │
│  ╚═══════════════════════════════════════════════════╝  │
└─────────────────────┬───────────────────────────────────┘
                      │ REST API (JSON)
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  💻 LOCAL WORKER                         │
│  ╔═══════════════════════════════════════════════════╗  │
│  ║  METATRADER 5 • ORDER EXECUTION • MONITORING     ║  │
│  ║  • Signal Validation                              ║  │
│  ║  • Position Management                            ║  │
│  ║  • Stop Loss / Take Profit                        ║  │
│  ╚═══════════════════════════════════════════════════╝  │
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ TECH STACK

<table>
<tr>
<td>

**🧠 BRAIN (Cloud)**
- Python 3.9+
- TensorFlow / Keras
- Google Vertex AI
- Cloud Storage
- BigQuery Analytics
- Custom Prediction Handler

</td>
<td>

**⚡ WORKER (Local)**
- MetaTrader 5 Terminal
- MQL5 Scripts
- Python MT5 Connector
- REST API Client
- Risk Management Module

</td>
</tr>
</table>

---

## 🎮 OPERATION STATUS

```yaml
Project: AKILES-1337 Sandbox
Phase: Development & Testing
Progress: [████████████████░░░░] 75%

Completed:
  ✅ Hybrid architecture designed
  ✅ LSTM model structure
  ✅ Vertex AI deployment framework
  ✅ Custom predictor.py handler
  ✅ MT5 connection module
  ✅ Base project structure

In Progress:
  🔄 Model training pipeline
  🔄 Risk management system
  🔄 Backtesting engine

Pending:
  ⏳ Live trading validation
  ⏳ Performance dashboard
  ⏳ Alert system
```

---

## 🚀 DEPLOYMENT PROTOCOL

### Prerequisites
```bash
# Clone the repo
git clone https://github.com/trece37/akiles-1337.git
cd akiles-1337

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# .\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration
```bash
# Set GCP credentials
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"

# Configure MT5 credentials (create config/mt5_config.json)
{
  "login": YOUR_MT5_LOGIN,
  "password": "YOUR_PASSWORD",
  "server": "YOUR_BROKER_SERVER"
}
```

### Execute
```bash
# Train LSTM model
python scripts/train_lstm.py --data data/XAUUSD_H1.csv --epochs 100

# Deploy to Vertex AI
python scripts/deploy_vertex.py --model models/lstm_v1

# Start MT5 worker
python scripts/mt5_worker.py --mode sandbox
```

---

## 📂 PROJECT STRUCTURE

```
akiles-1337/
├── 📁 src/
│   ├── models/              # LSTM architectures
│   ├── predictor.py         # Vertex AI custom handler
│   ├── mt5_connector/       # MetaTrader integration
│   └── utils/               # Helper functions
│
├── 📁 scripts/
│   ├── train_lstm.py        # Model training
│   ├── deploy_vertex.py     # Cloud deployment
│   ├── mt5_worker.py        # Local execution worker
│   └── backtest.py          # Strategy validation
│
├── 📁 docs/
│   ├── architecture.md      # System design docs
│   └── api_spec.md          # REST API documentation
│
├── 📁 proposals/
│   └── MODEL_PY/            # Experimental models
│
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md               # You are here
```

---

## 📊 PERFORMANCE TARGETS

```python
TARGET_METRICS = {
    'win_rate': '> 55%',           # Porcentaje de trades ganadores
    'profit_factor': '> 1.5',      # Ratio beneficio/pérdida
    'sharpe_ratio': '> 1.2',       # Risk-adjusted returns
    'max_drawdown': '< 15%',       # Pérdida máxima tolerada
    'avg_trade_duration': '4-8h',  # Duración promedio
    'risk_per_trade': '1-2%',      # Riesgo por operación
}
```

---

## ⚠️ DISCLAIMER

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  ⚠️  EXPERIMENTAL TRADING SYSTEM - USE AT YOUR OWN RISK  ║
║                                                           ║
║  • Este bot está en fase de desarrollo activo            ║
║  • Trading algorítmico conlleva riesgo de capital        ║
║  • No es asesoría financiera - DYOR                      ║
║  • Actualmente solo en modo SANDBOX                      ║
║  • Testea siempre en demo antes de ir a real             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 🧠 INTELLIGENCE & DATA

- **Market Data**: Yahoo Finance API, MT5 Historical Server
- **Features**: 50+ Technical Indicators (RSI, MACD, Bollinger, ATR...)
- **Timeframes**: M15, H1, H4, D1 multi-timeframe analysis
- **Training Data**: 2020-2024 XAU/USD historical prices
- **Model**: LSTM with attention mechanism

---

## 🔐 SECURITY

- 🔒 API keys almacenadas en GCP Secret Manager
- 🔒 Comunicación cifrada Brain ↔ Worker
- 🔒 Sin credenciales hardcoded en código
- 🔒 Repositorio privado - Acceso autorizado únicamente

---

## 🛠️ DEVELOPMENT ROADMAP

### Phase 1: Foundation ✅ DONE
- [x] Project structure
- [x] Basic LSTM model
- [x] MT5 connector
- [x] Vertex AI setup

### Phase 2: Core System 🔄 IN PROGRESS
- [ ] Advanced LSTM with attention
- [ ] Feature engineering pipeline
- [ ] Comprehensive backtesting
- [ ] Risk management system

### Phase 3: Production 🔜 UPCOMING
- [ ] Live trading (demo account)
- [ ] Performance monitoring dashboard
- [ ] Alert system (Telegram/Email)
- [ ] Auto-retraining pipeline

---

## 👤 AUTHOR

**Lead Developer**: [@trece37](https://github.com/trece37)  
**Location**: Spain 🇪🇸  
**Started**: December 2024  
**Status**: Active Development

---

<div align="center">

### 💀 BUILT BY TRADERS, FOR TRADERS 💀

```
╔═══════════════════════════════════════════════════════════╗
║  "In code we trust, in backtests we verify"              ║
║                                                           ║
║  AKILES-1337 • Proyecto Sandbox • v0.1-alpha             ║
╚═══════════════════════════════════════════════════════════╝
```

**[⚡ NOT PRODUCTION READY • FOR RESEARCH PURPOSES ONLY ⚡]**

---

*Made with 💻 and ☕ in late 2024*

</div>Trading bot con LSTM - Proyecto Akiles sandbox
## Objetivo
Bot de trading algorítmico usando redes LSTM para predicción de mercados.

## Tecnologías
- Python
- TensorFlow/Keras
- MetaTrader 5
- Google Cloud Platform

## Estado

En desarrollo. Este es el primer proyecto de una serie enfocada en trading algoritmico con inteligencia artificial. Actualmente se trabaja en la arquitectura base del modelo LSTM, la conexion con MetaTrader 5 y la integracion con servicios de Google Cloud Platform para procesamiento y despliegue.
