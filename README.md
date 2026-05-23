# 🩺 DiaBeat AI: REST API Core Service (Version 1.2.2)

[![Deployment Status](https://img.shields.io/badge/Deployment-Hugging%20Face%20Spaces-FFD21E.svg?style=for-the-badge&logo=huggingface)](https://chivasy1-diabeat-api.hf.space/docs)
[![Framework Status](https://img.shields.io/badge/Framework-FastAPI-009688.svg?style=for-the-badge&logo=fastapi)](https://chivasy1-diabeat-api.hf.space/docs)
[![Engine Status](https://img.shields.io/badge/Engine-TensorFlow%202.x-FF6F00.svg?style=for-the-badge&logo=tensorflow)](https://chivasy1-diabeat-api.hf.space/docs)

Ini adalah RESTful API sistem **DiaBeat AI** berbasis Kecerdasan Buatan (AI) versi `1.2.2` yang dirancang untuk mendeteksi risiko diabetes secara dini. Proyek ini mengintegrasikan model **Deep Learning** (TensorFlow Functional API) dengan **FastAPI** serta LLM Generative AI untuk asisten konsultasi pintar.

## 🔗 Dokumentasi & Tautan Penting
* **Live API Interactive Docs (Hugging Face):** [DiaBeat AI Live Swagger UI](https://chivasy1-diabeat.hf.space/docs#/) 🚀
* **Panduan Penggunaan Fitur:** [Pindah ke API_DOCUMENTATION.md](API_DOCUMENTATION.md) 📖
* **Instruksi Jalankan Lokal:** [Pindah ke INSTALLATION.md](INSTALLATION.md) 🛠️

## 🚀 Fitur Utama
- **AI-Powered Prediction**: Menggunakan model Deep Learning ANN dengan teknik optimasi tingkat lanjut logits untuk klasifikasi biner.
- **Pre-processing Terintegrasi**: Menggunakan `StandardScaler` biner aktif untuk memastikan data input selalu sesuai dengan skala standar model.
- **AI Consultation Chatbot**: Integrasi asisten pintar bertenaga Gemini API untuk sesi dialog edukasi medis terisolasi.
- **Skalabilitas**: Dibangun di atas FastAPI yang mendukung proses asinkron untuk performa tinggi produksi.

## 📂 Struktur Proyek Terupdate (v1.2.2)
```text
.
├── main.py                                 # Server API utama (FastAPI)
├── diabeat_model_production(v1.2.2).keras  # Mesin Utama Model ANN (Logits Output)
├── diabeat_model_production(v1.2).keras    # Mesin Cadangan Fail-Safe Server
├── scaler.pkl                              # Objek normalisasi data StandardScaler
├── logs/                                   # Folder log metrik pelatihan TensorBoard
├── requirements.txt                        # Daftar dependensi Python
├── Dockerfile                              # Konfigurasi pembentukan image kontainer
├── API_DOCUMENTATION.md                    # Panduan teknis penggunaan endpoint
└── INSTALLATION.md                         # Instruksi penyiapan lingkungan lokal

```

## 🛠️ Stack Teknologi

* **Core**: Python 3.12 (Diwajibkan untuk TensorFlow Core compatibility)
* **Machine Learning**: TensorFlow 2.x, Scikit-Learn, Joblib
* **Generative AI Engine**: Google GenerativeAI (Gemini v1.5/2.5 Flash)
* **API Framework & Server**: FastAPI, Pydantic, Uvicorn, Gunicorn
* **Data Handling**: NumPy, Pandas
