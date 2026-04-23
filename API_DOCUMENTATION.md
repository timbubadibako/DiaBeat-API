# 📖 Dokumentasi API DiaBeat
Dokumentasi ini menjelaskan cara berinteraksi dengan layanan AI DiaBeat untuk melakukan prediksi risiko diabetes.
---
## 🌐 Informasi Server
* **Base URL:** `http://127.0.0.1:8000`
* **Format Data:** `JSON`
* **Metode Utama:** `POST`
---
## 🛠️ Daftar Endpoint

### 1. Health Check
Digunakan untuk memastikan server API berjalan dengan baik.
* **URL:** `/`
* **Method:** `GET`
* **Response:**
  ```json
  {
    "message": "DiaBeat AI API is Online!"
  }
  ```

---

### 2. Prediksi Risiko Diabetes
Endpoint utama untuk mengirim data medis dan menerima hasil klasifikasi dari model Deep Learning.

* **URL:** `/predict`
* **Method:** `POST`
* **Payload (JSON Body):**

| Field | Tipe | Deskripsi | Nilai Representasi |
| :--- | :--- | :--- | :--- |
| `Gender` | int | Jenis Kelamin | `0`: Female, `1`: Male |
| `Age` | int | Usia | Angka bulat (contoh: 25) |
| `Physical_Activity`| int | Tingkat Aktivitas | `0`: Low, `1`: Moderate, `2`: High |
| `Smoking_Status` | int | Status Merokok | `0`: Never, `1`: Former, `2`: Current |
| `Alcohol_Intake` | int | Konsumsi Alkohol | `0`: None, `1`: Occasional, `2`: Regular |
| `Glucose` | float | Gula Darah | Angka desimal (mg/dL) |
| `Blood_Pressure` | float | Tekanan Darah | Angka desimal (mmHg) |
| `Skin_Thickness` | float | Tebal Kulit | Angka desimal (mm) |
| `Insulin` | float | Kadar Insulin | Angka desimal (mu U/ml) |
| `BMI` | float | Indeks Massa Tubuh| Angka desimal (kg/m²) |
| `Cholesterol` | float | Kolesterol | Angka desimal (mg/dL) |
| `Diabetes_Pedigree`| float | Riwayat Genetik | Angka desimal (skor 0.0 - 2.5) |
| `Family_History` | int | Riwayat Keluarga | `0`: Tidak, `1`: Ya |
| `Hypertension` | int | Hipertensi | `0`: Tidak, `1`: Ya |

---
## 📥 Contoh Penggunaan (Request)

**Request Body:**
```json
{
  "Gender": 1,
  "Age": 45,
  "Physical_Activity": 1,
  "Smoking_Status": 1,
  "Alcohol_Intake": 0,
  "Glucose": 145.5,
  "Blood_Pressure": 90,
  "Skin_Thickness": 20,
  "Insulin": 85,
  "BMI": 28.4,
  "Cholesterol": 210,
  "Diabetes_Pedigree": 0.52,
  "Family_History": 1,
  "Hypertension": 0
}
```

---

## 📤 Contoh Tanggapan (Response)

**Response Success (200 OK):**
```json
{
  "status": "success",
  "prediction": {
    "risk_score": 82.45,
    "is_diabetic": true,
    "label": "Diabetic"
  }
}
```

**Keterangan Response:**
* `risk_score`: Persentase tingkat risiko (0.0 - 100.0).
* `is_diabetic`: Boolean hasil klasifikasi (True jika risiko > 50%).
* `label`: Kategori hasil prediksi dalam bentuk teks.

---

## ⚠️ Error Handling
Jika terjadi kesalahan, API akan mengirimkan kode status berikut:
* `422 Unprocessable Entity`: Data JSON tidak lengkap atau tipe data salah.
* `500 Internal Server Error`: Kegagalan pada sisi server atau model AI gagal memproses data.
