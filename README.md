# 🩺 DiaBeat-API: Diabetes Risk Prediction Service

Ini adalah RESTful API sistem DiaBeat berbasis Kecerdasan Buatan (AI) yang dirancang untuk mendeteksi risiko diabetes secara dini. Proyek ini mengintegrasikan model **Deep Learning** (TensorFlow Functional API) dengan **FastAPI** untuk menyediakan layanan prediksi yang cepat, akurat, dan mudah diintegrasikan ke berbagai platform kesehatan.

## 🚀 Fitur Utama
- **AI-Powered Prediction**: Menggunakan model Deep Learning yang dilatih dengan teknik optimasi tingkat lanjut.
- **Pre-processing Terintegrasi**: Menggunakan `StandardScaler` yang dipaketkan untuk memastikan data input selalu sesuai dengan skala standar model.
- **Dokumentasi Interaktif**: Dilengkapi dengan Swagger UI untuk pengujian endpoint secara real-time.
- **Skalabilitas**: Dibangun di atas FastAPI yang mendukung proses asinkron untuk performa tinggi.

## 📂 Struktur Proyek
```text
.
├── main.py                # Server API utama (FastAPI)
├── baru/                  # Direktori penyimpanan aset model
│   ├── diabeat_model_production(v1.2).keras
│   └── scaler.pkl         # Objek normalisasi data
├── requirements.txt       # Daftar dependensi Python
├── API_DOCUMENTATION.md   # Panduan teknis penggunaan endpoint
├── INSTALLATION.md        # Instruksi penyiapan lingkungan lokal
└── .gitignore             # Konfigurasi pengabaian file Git
```

## 🛠️ Stack Teknologi
- **Core**: Python 3.11+
- **Machine Learning**: TensorFlow, Keras, Scikit-Learn
- **API Framework**: FastAPI & Uvicorn
- **Data Handling**: NumPy, Pandas, Joblib


