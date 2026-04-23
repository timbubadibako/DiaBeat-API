# 🛠️ Panduan Instalasi & Kolaborasi (Untuk Tim)

Dokumentasi ini ditujukan bagi anggota tim yang ingin menjalankan atau mengembangkan layanan **DiaBeat API** di lingkungan lokal masing-masing.

## 📋 Prasyarat
Sebelum memulai, pastikan kamu sudah menginstal:
* **Python 3.11 atau 3.12** (Sangat disarankan untuk menghindari konflik library TensorFlow).
* **Git** (Untuk mengelola kode).

---

## 🚀 Langkah-Langkah Setup

### 1. Ambil Kode dari GitHub
Buka terminal/command prompt, arahkan ke folder kerjamu, lalu jalankan:
```bash
git clone [https://github.com/timbubadibako/DiaBeat-API.git](https://github.com/timbubadibako/DiaBeat-API.git)
cd DiaBeat-API
```

### 2. Membuat Virtual Environment (venv)
Sangat penting untuk menggunakan `venv` agar versi Python dan library tidak berantakan dengan proyek lain di laptopmu.

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
*Tanda berhasil: Muncul tulisan `(venv)` di sebelah kiri prompt terminalmu.*

### 3. Instalasi Library (Dependensi)
Semua library yang dibutuhkan (FastAPI, TensorFlow, dll) sudah didaftarkan di dalam `requirements.txt`. Kamu hanya perlu menjalankan satu perintah:
```bash
pip install -r requirements.txt
```

### 4. Menjalankan Server API
Setelah semua library terinstal, nyalakan server dengan perintah:
```bash
uvicorn main:app --reload
```
Server akan berjalan di: `http://127.0.0.1:8000`

---

## 🧪 Cara Mengetes API Secara Mandiri
1. Buka browser dan akses: `http://127.0.0.1:8000/docs`.
2. Kamu akan masuk ke **Swagger UI**.
3. Cari rute **POST /predict**, klik **Try it out**.
4. Masukkan data JSON contoh, lalu klik **Execute**.
5. Jika muncul respon JSON berisi `risk_score`, berarti setup kamu sudah berhasil!

---

## 🤝 Alur Kontribusi (Git Workflow)
Jika kamu melakukan perubahan kode:
1. Pastikan selalu lakukan `git pull origin main` sebelum mulai bekerja.
2. Buat branch baru jika ingin menambah fitur: `git checkout -b fitur-baru-kamu`.
3. Setelah selesai, lakukan `commit` dan `push`.
