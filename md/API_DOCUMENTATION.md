# 📖 Panduan Dokumentasi REST API

Panduan ini ditujukan bagi pengembang backend (Express.js) atau Frontend yang ingin mengintegrasikan layanan prediksi DiaBeat AI ke dalam aplikasi.

## 🔗 Tautan Navigasi Cepat
* [Kembali ke Halaman Utama README](README.md)
* [Lihat Panduan Instalasi Lokal](INSTALLATION.md)
* **Live Server Sandbox:** [DiaBeat AI HF Production Docs](https://chivasy1-diabeat.hf.space/docs#/)

## 🌐 Informasi Peladen
* **Local Development Base URL:** `http://localhost:8000`
* **Production Cloud Base URL:** `https://chivasy1-diabeat.hf.space`
* **Format Pertukaran Data:** `JSON`

---

## 🛠️ Spesifikasi Detail Endpoint

### 1. POST `/predict` (Skrining Risiko Diabetes)
Mengirimkan array 14 elemen data fitur klinis pasien hasil pemetaan encoder backend untuk dianalisis oleh model ANN.

#### **Request Body (`JSON`)**
```json
{
  "features": [1, 45, 1, 0, 1, 110, 80, 20, 85, 27.5, 200, 0.627, 1, 0],
  "context": "Pasien mengeluhkan sering merasa haus dan frekuensi buang air kecil meningkat tajam akhir-akhir ini."
}

```

*Note: Atribut `context` bersifat opsional dan berguna untuk memberikan instruksi keluhan tambahan ke generator rekomendasi AI.*

#### **Response Body (`JSON`)**

*Output dijamin patuh dengan aturan schema validator Joi.*

```json
{
  "prediction": "Non-diabetic",
  "probability": 0.2314,
  "recommendation": "Pertahankan pola makan tinggi serat saat ini dan lakukan olahraga kardio ringan secara teratur 3 kali seminggu."
}

```

### 2. POST `/consultation` (Asisten Chatbot AI Medis)

Endpoint interaktif khusus tanya-jawab seputar tindakan preventif bahaya diabetes dan regulasi pola hidup sehat.

#### **Request Body (`JSON`)**

```json
{
  "message": "Bagaimana cara mengatur pola makan yang aman jika saya memiliki riwayat keturunan diabetes?"
}

```

#### **Response Body (`JSON`)**

```json
{
  "status_code": 200,
  "ai_response": "Fokus pada makanan berindeks glikemik rendah seperti karbohidrat kompleks... [Edukasi Medis]... Catatan: Layanan ini merupakan media edukasi dini, tetap konsultasikan dengan fasilitas medis resmi."
}

```

---

## ⚠️ Penanganan Galat (Error Handling)

Server akan melemparkan kode status `500 Internal Server Error` jika tipe data fitur di dalam array tidak selaras atau jumlah indeks elemen kurang dari 14 parameter standar operasional model.