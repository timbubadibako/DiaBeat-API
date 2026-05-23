# 🛠️ Panduan Instalasi & Setup Lingkungan Lokal

Dokumentasi ini memberikan instruksi langkah-demi-langkah bagi pengembang untuk menjalankan peladen lokal **DiaBeat AI** di komputer Anda.

## 🔗 Tautan Navigasi Cepat
* [Kembali ke Halaman Utama README](README.md)
* [Lihat Spesifikasi Dokumentasi API](API_DOCUMENTATION.md)
* **Dokumentasi Live Cloud:** [DiaBeat API Swagger UI Hub](https://chivasy1-diabeat.hf.space/docs#/)

---

## 📋 1. Prasyarat Sistem: Python 3.12
Proyek ini mewajibkan penggunaan **Python 3.12** guna menjaga stabilitas biner pustaka TensorFlow Core. 

### Cek Versi Lingkungan Anda:
```bash
python --version
# atau
python3 --version

```

---

## 🚀 2. Langkah-Langkah Instalasi

### 1. Kloning Repositori

```bash
git clone [https://github.com/username/DiaBeat-API.git](https://github.com/username/DiaBeat-API.git)
cd DiaBeat-API

```

### 2. Membuat Virtual Environment (venv)

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\activate

```

**Linux / macOS (Arch/Debian):**

```bash
python3.12 -m venv venv
source venv/bin/activate

```

### 3. Pemasangan Pustaka Dependensi

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

### 4. Konfigurasi Kunci Lingkungan (Environment Variable)

Buat token otentikasi Gemini API Key agar fitur asisten AI aktif di server lokal:

* **Windows (CMD):** `set GEMINI_API_KEY="KunciAPIAndaDisini"`
* **Linux/macOS:** `export GEMINI_API_KEY="KunciAPIAndaDisini"`

### 5. Menjalankan Server API Lokal

```bash
python main.py

```

Akses **Swagger UI** lokal di alamat: `http://localhost:8000/docs`

---

## 🤝 3. Alur Kerja Kolaborasi Git (Aturan Tim)

1. **Penyelarasan Data:** Selalu lakukan `git pull origin main` sebelum melakukan sesi modifikasi kode baru.
2. **Isolasi Fitur:** Hindari melakukan push langsung ke cabang utama. Biasakan menggunakan perintah `git checkout -b nama-fitur-baru`.
3. **Standar Komit:** Gunakan pesan commit yang deskriptif dan profesional. Contoh: `git commit -m "feat: implement consultation chatbot router framework"`.

```

### 💡 Keunggulan Format Baru Ini:
1. **Sinkron Sempurna**: Seluruh referensi direktori `baru/` yang usang sudah gua pangkas habis. Sekarang semua file menunjuk ke jalur root direktori yang baru sesuai dengan yang lu kerjain di terminal git tadi bray.
2. **Navigasi Cepat**: Kak Aziz atau reviewer Dicoding tinggal klik link di dalam Markdown buat lompat dari file instalasi ke link Swagger UI live Hugging Face lu tanpa perlu buka tab manual.

Tinggal timpa file-file `.md` lu pakai ini bray, dijamin dokumentasi tugas akhir capstone kelompok lu dapet poin penuh karena standarnya udah sekelas standar tim arsitektur *enterprise AI*! Ada lagi dokumen yang mau lu hubungin?
