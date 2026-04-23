# DiaBeat-API : Diabetes Risk Prediction Service

DiaBeat adalah layanan berbasis Kecerdasan Buatan (AI) yang dirancang untuk mendeteksi risiko diabetes secara dini. Proyek ini menggunakan arsitektur **Deep Learning** yang dideploy sebagai RESTful API untuk kebutuhan integrasi aplikasi kesehatan.

## 🚀 Fitur Utama
- **Deep Learning Model**: Dibangun menggunakan TensorFlow Functional API.
- **Custom Optimization**: Implementasi Custom Callback untuk efisiensi training.
- **FastAPI Framework**: Layanan API asinkron dengan performa tinggi.
- **Automated Scaling**: Integrasi `StandardScaler` untuk akurasi prediksi yang konsisten.

## 🛠️ Stack Teknologi
- **Language**: Python 3.11/3.12
- **AI Framework**: TensorFlow & Keras
- **Web Framework**: FastAPI
- **Data Science**: Pandas, NumPy, Scikit-learn, Joblib
- **Server**: Uvicorn

## 📂 Struktur Folder
```text
.
├── main.py                         # Entry point API (FastAPI)
├── diabeat_model_production.keras  # Trained Deep Learning Model
├── scaler.pkl                      # Object Scaler (Preprocessing)
├── requirements.txt                # Daftar library/dependensi
├── .gitignore                      # File untuk mengabaikan venv/
└── README.md                       # Dokumentasi proyek
