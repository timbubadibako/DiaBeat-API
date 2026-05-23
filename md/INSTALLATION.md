# 🛠️ Panduan Instalasi & Setup Lingkungan

Dokumentasi ini memberikan instruksi langkah-demi-langkah bagi pengembang untuk menjalankan **DiaBeat API** di berbagai sistem operasi.

---

## 📋 1. Prasyarat: Python 3.12
Proyek ini mewajibkan **Python 3.12**. Versi di atasnya (seperti 3.14) belum didukung secara resmi oleh TensorFlow dan akan menyebabkan error saat instalasi.

### Cek Versi Python Anda:
Buka terminal/command prompt dan ketik:
```bash
python --version
# atau
python3 --version

```

### Jika Belum Memiliki Python 3.12, Ikuti Panduan Ini:

#### **A. Linux (Arch Linux / Manjaro)**

Arch biasanya menggunakan versi terbaru. Jika `python` Anda versi 3.13+, instal versi 3.12 melalui AUR:

```bash
sudo pacman -S python312

```

#### **B. Windows**

1. Unduh installer Python 3.12 dari [python.org](https://www.python.org/downloads/windows/).
2. **PENTING:** Saat instalasi, centang kotak **"Add Python to PATH"**.
3. Selesaikan instalasi.

#### **C. macOS**

Gunakan [Homebrew](https://brew.sh/):

```bash
brew install python@3.12

```

---

## 🚀 2. Langkah-Langkah Instalasi

### 1. Kloning Repositori

```bash
git clone [https://github.com/username/DiaBeat-API.git](https://github.com/username/DiaBeat-API.git)
cd DiaBeat-API

```

### 2. Membuat Virtual Environment (venv)

Gunakan Python 3.12 secara spesifik saat membuat environment.

**Windows:**

```powershell
python -m venv venv
.\venv\Scripts\activate

```

**Linux / macOS:**

```bash
# Jika python312 adalah command-nya
python3.12 -m venv venv
source venv/bin/activate

```

*Pastikan muncul indikator `(venv)` di terminal Anda.*

### 3. Instalasi Dependensi

Pastikan pip sudah dalam versi terbaru sebelum menginstal library:

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

### 4. Menjalankan Server API

Jalankan langsung melalui entry point `main.py`:

```bash
python main.py

```

API akan aktif di: `http://localhost:8000`

---

## 🧪 3. Pengujian API (Interactive Docs)

Tanpa perlu Postman, Anda bisa mengetes API langsung melalui browser:

1. Buka: `http://localhost:8000/docs`.
2. Anda akan melihat **Swagger UI**.
3. Klik **POST /predict** -> **Try it out**.
4. Gunakan payload JSON default, lalu klik **Execute**.
5. Respon sukses akan menampilkan `prediction` dan `probability` (2 angka desimal).

---

## 🤝 4. Alur Kerja Git (Tim)

1. **Update:** Selalu `git pull origin main` sebelum mulai koding.
2. **Branch:** Jangan langsung push ke main. Gunakan `git checkout -b fitur-kamu`.
3. **Commit:** Gunakan pesan yang jelas, contoh: `git commit -m "feat: tambah validasi input"`.