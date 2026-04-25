# 🛠️ Panduan Instalasi & Setup Lingkungan

Dokumentasi ini memberikan instruksi langkah-demi-langkah bagi pengembang yang ingin menjalankan atau berkontribusi pada layanan **DiaBeat API** di lingkungan lokal.

## 📋 Prasyarat
Sebelum memulai, pastikan sistem Anda sudah terinstal:
* **Python 3.11 atau 3.12** (Sangat disarankan untuk kompatibilitas optimal TensorFlow).
* **Git** (Untuk manajemen versi kode).

---

## 🚀 Langkah-Langkah Instalasi

### 1. Kloning Repositori
Buka terminal atau command prompt, navigasikan ke direktori kerja Anda, lalu jalankan:
```bash
git clone [https://github.com/username/DiaBeat-API.git](https://github.com/username/DiaBeat-API.git)
cd DiaBeat-API
```

### 2. Konfigurasi Lingkungan Virtual (Virtual Environment)
Disarankan menggunakan `venv` untuk menjaga isolasi dependensi agar tidak berbenturan dengan proyek lain.

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
*Catatan: Jika berhasil, indikator `(venv)` akan muncul di sebelah kiri prompt terminal Anda.*

### 3. Instalasi Dependensi
Instal semua pustaka yang diperlukan (FastAPI, TensorFlow, Scikit-Learn, dll.) melalui file `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Menjalankan Server API
Layanan ini sudah dikonfigurasi untuk berjalan langsung melalui entry point `main.py`. Jalankan perintah berikut:
```bash
python main.py
```
Server akan aktif di: `http://localhost:8000`

---

## 🧪 Pengujian API (Interactive Docs)
Proyek ini dilengkapi dengan dokumentasi interaktif otomatis. Untuk melakukan pengujian tanpa alat tambahan (seperti Postman):

1. Buka browser dan akses: `http://localhost:8000/docs`.
2. Anda akan diarahkan ke halaman **Swagger UI**.
3. Temukan rute **POST /predict**, lalu klik tombol **"Try it out"**.
4. Gunakan contoh payload JSON yang tersedia, lalu klik **"Execute"**.
5. Jika API mengembalikan respon berupa `prediction` dan `probability`, berarti instalasi Anda sukses!

---

## 🤝 Alur Kerja Pengembangan (Git Workflow)
Bagi Anda yang ingin berkontribusi, harap ikuti alur berikut:
1. Lakukan pembaruan kode lokal dengan `git pull origin main`.
2. Gunakan branch baru untuk fitur atau perbaikan: `git checkout -b nama-fitur`.
3. Lakukan pengujian lokal sebelum melakukan `commit` dan `push` kembali ke repositori.