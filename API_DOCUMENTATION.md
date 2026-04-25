# 📖 Panduan Dokumentasi API

Panduan ini ditujukan bagi pengembang yang ingin mengintegrasikan layanan prediksi DiaBeat ke dalam aplikasi Frontend, Mobile, atau layanan pihak ketiga lainnya.

## 🌐 Informasi Endpoint
* **Base URL:** `http://localhost:8000`
* **Format Pertukaran Data:** `JSON`
* **Interactive Docs:** `/docs` (Swagger UI) atau `/redoc`

---

## 🛠️ Endpoint: Prediksi Risiko

### POST `/predict`
Mengirimkan data klinis pasien untuk mendapatkan hasil analisis risiko diabetes.

#### **Request Body**
Gunakan format `features` dalam bentuk list angka. Pastikan urutan data sesuai dengan protokol input berikut:

**Urutan Fitur (Index 0-13):**
1. Gender (1: L, 0: P) | 2. Age | 3. Physical Activity | 4. Smoking | 5. Alcohol | 6. Glucose | 7. Blood Pressure | 8. Skin Thickness | 9. Insulin | 10. BMI | 11. Cholesterol | 12. Pedigree | 13. Family History | 14. Hypertension

**Contoh Payload:**
```json
{
  "features": [1, 45, 1, 0, 0, 125.5, 80.0, 20.0, 85.0, 28.4, 190.0, 0.45, 1, 0]
}
```

#### **Response Body**
API akan mengembalikan klasifikasi risiko dan tingkat probabilitas keyakinan model.

**Contoh Tanggapan Sukses:**
```json
{
  "prediction": "Diabetic",
  "probability": 0.89
}
```

---

## ⚠️ Penanganan Error
API akan mengembalikan status code `500` jika terjadi ketidaksesuaian jumlah fitur input (misal: mengirim kurang atau lebih dari 14 parameter).
```

---

### **3. INSTALLATION.md**
```text
# 🛠️ Panduan Instalasi Proyek

Ikuti langkah-langkah di bawah ini untuk menjalankan layanan DiaBeat API di lingkungan lokal Anda.

### 1. Persiapan Repositori
Clone proyek ini ke mesin lokal Anda menggunakan Git:
```bash
git clone [https://github.com/username/DiaBeat-API.git](https://github.com/username/DiaBeat-API.git)
cd DiaBeat-API
```

### 2. Lingkungan Virtual (Virtual Environment)
Disarankan menggunakan `venv` untuk menjaga isolasi dependensi:
```bash
# Membuat venv
python -m venv venv

# Aktivasi (Windows)
.\venv\Scripts\activate

# Aktivasi (Mac/Linux)
source venv/bin/activate
```

### 3. Instalasi Dependensi
Instal semua pustaka yang diperlukan (TensorFlow, FastAPI, dll.):
```bash
pip install -r requirements.txt
```

### 4. Menjalankan Layanan
Proyek ini telah dikonfigurasi untuk berjalan langsung melalui file utama:
```bash
python main.py
```
Setelah berjalan, akses **Swagger UI** di `http://localhost:8000/docs` untuk melakukan simulasi request secara interaktif.
