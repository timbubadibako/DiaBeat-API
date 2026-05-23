# =====================================================================
# PRODUCTION API: DIABEAT AI (FULL FINAL VERSION 1.2.2)
# =====================================================================
import os
import joblib
import numpy as np
import tensorflow as tf
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import google.generativeai as genai
from dotenv import load_dotenv

# --- TRICK CERDAS FAIL-SAFE DOTENV UNTUK MULTI-ENVIRONMENT CONTROL ---
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("[INFO] Lingkungan Lokal: File .env sukses dimuat ke sistem.")
except ModuleNotFoundError:
    print("[INFO] Lingkungan Cloud: Mengabaikan python-dotenv, beralih menggunakan Secrets Native HF.")
# ---------------------------------------------------------------------

# 1. INISIALISASI FASTAPI WITH METADATA RESMI SYSTEM
app = FastAPI(
    title="DiaBeat AI REST API",
    description="""
    Peladen API Produksi Terintegrasi Kustom Deep Learning ANN & Generative AI.
    
    ### 📊 Pemantauan Grafik & Manajemen Model:
    * **TensorBoard Dashboard:** Dapat diakses secara live via tab bawaan di Hugging Face Spaces.
    * **Model Core Engine Active:** v1.2.2 (Dengan Logits Optimization & Fail-Safe Auto Fallback).
    """,
    version="1.2.2"
)

# 2. PENGATURAN KEBIJAKAN CORS (CROSS-ORIGIN RESOURCE SHARING)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. KONFIGURASI SECURE KONEKSI GEMINI API (SDK GOOGLE GEN-AI)
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    print("[SUCCESS] Google Gemini API Key Terdeteksi & Sukses Dikonfigurasi!")
else:
    print("[WARNING] 'GEMINI_API_KEY' Tidak Ditemukan! Fitur asisten pintar akan memakai teks default medis.")

# Indikator global untuk melacak mesin model yang aktif di peladen
ACTIVE_MODEL_VERSION = None

# 4. MUAT BERKAS MODEL & SCALER DENGAN MEKANISME FAIL-SAFE (FALLBACK)
try:
    # Memuat parameter normalisasi fitur StandardScaler
    scaler = joblib.load("scaler.pkl")
    
    # Mencoba memuat mesin model utama v1.2.2 yang berbasis logits kustom loop
    model = tf.keras.models.load_model("diabeat_model_production(v1.2.2).keras", compile=False)
    ACTIVE_MODEL_VERSION = "v1.2.2"
    print("[SUCCESS] Mesin Utama Model v1.2.2 Sukses Mengudara!")

except Exception as e_primary:
    print(f"[WARNING] Gagal memuat mesin utama v1.2.2: {e_primary}")
    print("[FALLBACK] Mencoba mengaktifkan mesin cadangan model v1.2 lama...")
    try:
        model = tf.keras.models.load_model("diabeat_model_production(v1.2).keras", compile=False)
        ACTIVE_MODEL_VERSION = "v1.2"
        print("[SUCCESS] Fail-Safe Aktif: Mesin Cadangan Model v1.2 Berhasil Mengudara!")
    except Exception as e_fatal:
        print(f"[CRITICAL ERROR] Server AI Lumpuh Total! Berkas aset pkl/keras tidak ditemukan: {e_fatal}")


# =====================================================================
# DEFINISI SKEMA VALIDASI DATA ENCODING & CHATBOT (PYDANTIC SCHEMAS)
# =====================================================================

class PatientDataInput(BaseModel):
    """Skema validasi 14 elemen data fitur klinis pasien dan teks keluhan dari backend."""
    features: list = Field(
        ..., 
        example=[1, 45, 1, 0, 1, 110, 80, 20, 85, 27.5, 200, 0.627, 1, 0],
        description="Urutan Fitur: Gender, Age, Activity, Smoking, Alcohol, Glucose, BP, Thickness, Insulin, BMI, Chol, Pedigree, Family, Hypertension"
    )
    context: Optional[str] = Field(
        None, 
        example="Pasien mengeluhkan sering merasa haus dan frekuensi buang air kecil meningkat tajam akhir-akhir ini.",
        description="Keluhan klinis atau teks kontekstual tambahan langsung dari formulir pasien."
    )

class PredictionResponse(BaseModel):
    """Skema luaran hasil prediksi klasifikasi risiko patuh spesifikasi Joi Validator."""
    prediction: str
    probability: float
    recommendation: str

class ChatbotConsultationInput(BaseModel):
    """Skema masukan untuk endpoint interaktif chatbot medis."""
    message: str = Field(..., description="Pertanyaan atau keluhan terkait diabetes dari pasien.")

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Bagaimana cara mengatur pola makan yang aman jika saya memiliki riwayat keturunan diabetes?"
            }
        }

class ChatbotConsultationResponse(BaseModel):
    """Skema tanggapan luaran dari asisten AI klinis."""
    status_code: int
    ai_response: str


# =====================================================================
# INTERNAL ENGINE LOGIC (MATHEMATICS & LLM INFERENCE)
# =====================================================================

def manual_sigmoid(logits):
    """Mengubah nilai linear logits kaku menjadi representasi desimal probabilitas."""
    return 1 / (1 + np.exp(-logits))

def generate_health_advice(prediction_label, probability, patient_context):
    """Menghasilkan 1 kalimat rekomendasi klinis singkat menggunakan Gemini API."""
    if not GOOGLE_API_KEY:
        return "Segera konsultasikan hasil skrining awal ini dengan dokter spesialis terdekat untuk evaluasi medis menyeluruh."
        
    try:
        # Menggunakan model generasi terbaru gemini-2.5-flash yang super cepat dan stabil
        gemini_model = genai.GenerativeModel('gemini-2.5-flash')
        complaint_text = patient_context if patient_context else "Tidak ada keluhan spesifik yang dilaporkan oleh pasien."
        
        prompt = f"""
        Anda adalah seorang dokter spesialis endokrinologi yang bijaksana.
        Seorang pasien melakukan screening risiko diabetes menggunakan model kecerdasan buatan dengan hasil:
        - Label Diagnosis: {prediction_label}
        - Probabilitas Risiko: {probability * 100:.2f}%
        - Catatan Keluhan: {complaint_text}
        
        Berikan 1 kalimat rekomendasi medis awal atau perbaikan pola hidup yang singkat, menenangkan, dan edukatif.
        ATURAN KETAT: Jangan gunakan poin-poin, jangan gunakan tanda bintang (*), jangan gunakan markdown tebal/miring.
        Tuliskan langsung satu baris kalimat teks murni saja (maksimal 20 kata).
        """
        
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
        print(f"[ERROR GEMINI INTEGRATION] Gagal memanggil LLM Core (Advice): {e}")
        return "Segera lakukan pemeriksaan laboratorium klinis resmi untuk konfirmasi diagnosis medis Anda."


# =====================================================================
# IMPLEMENTASI ROUTER ENDPOINT CORE
# =====================================================================

@app.get("/", tags=["Status Peladen"])
def read_root():
    """Endpoint Health Check untuk melacak kesiapan mesin model ANN dan status LLM."""
    return {
        "status": "Online",
        "active_engine": ACTIVE_MODEL_VERSION,
        "gen_ai_status": "Connected" if GOOGLE_API_KEY else "Disconnected",
        "tensorboard_logs": "Detected (Sync Active via HF Spaces Hub)"
    }


@app.post("/predict", response_model=PredictionResponse, status_code=status.HTTP_200_OK, tags=["Analisis Prediksi"])
def predict_diabetes_risk(data: PatientDataInput):
    """
    Endpoint utama prediksi risiko diabetes. Menerima array 14 elemen hasil mapper backend,
    menormalisasi data, memprediksi risiko, dan memberikan rekomendasi berbasis AI secara real-time.
    """
    if ACTIVE_MODEL_VERSION is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Mesin inferensi gagal diaktifkan. Periksa ketersediaan berkas model .keras di root."
        )

    try:
        # 1. Transformasi array 1D masukan menjadi matriks 2D NumPy Array
        input_features = np.array([data.features])
        
        # 2. Penyelarasan Skala Data Fitur numerik menggunakan parameter StandardScaler
        scaled_features = scaler.transform(input_features)
        
        # 3. Operasi Forward Pass Evaluasi Model ANN
        prediction = model.predict(scaled_features, verbose=0)
        
        # 4. Penjinakan Nilai Output Berdasarkan Versi Mesin yang Aktif
        if ACTIVE_MODEL_VERSION == "v1.2.2":
            # Model v1.2.2 bertipe logits murni, wajib dilewatkan ke rumus sigmoid manual bray!
            probability_value = float(manual_sigmoid(prediction[0][0]))
        else:
            # Model v1.2 lama sudah memiliki lapisan aktivasi internal di layer keluaran
            probability_value = float(prediction[0][0])
            
        # 5. Pembulatan Presisi Desimal (Format 4 angka di belakang koma)
        probability_value = float("{:.4f}".format(probability_value))
        
        # 6. Pemetaan Label String Klasifikasi Biner Patuh Validasi Enum Joi Backend
        prediction_label = "Diabetic" if probability_value >= 0.5 else "Non-diabetic"
        
        # 7. Pemanggilan Engine LLM Generative AI untuk Mengisi Atribut Rekomendasi
        ai_recommendation = generate_health_advice(prediction_label, probability_value, data.context)
        
        return PredictionResponse(
            prediction=prediction_label,
            probability=probability_value,
            recommendation=ai_recommendation
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi interupsi pada proses kalkulasi matriks internal: {str(e)}"
        )


@app.post("/consultation", status_code=status.HTTP_200_OK, tags=["Asisten Chatbot AI"])
def medical_chatbot_consultation(user_input: ChatbotConsultationInput):
    """
    Endpoint asisten interaktif dialog konsultasi seputar edukasi pencegahan diabetes.
    Ditenagai oleh LLM Gemini-2.5-Flash dengan proteksi guardrail pembatasan konteks.
    """
    if not GOOGLE_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Layanan asisten pintar dinonaktifkan sementara karena kunci API belum terpasang."
        )

    try:
        # KUNCI UTAMA: PENAMBAHAN ATURAN BATASAN KONTEKS (GUARDRAIL KETAT)
        system_instruction = (
            "Anda adalah DiaBeat Asisten AI Medis, seorang dokter spesialis penyakit dalam dan endokrinologi yang taktis dan profesional.\n\n"
            "BATASAN KONTEKS MUTLAK:\n"
            "1. Tugas utama Anda HANYA menjawab pertanyaan seputar diabetes, regulasi gula darah, manajemen pola makan sehat, "
            "aktivitas fisik preventif, dan penyakit dalam/metabolik yang berkaitan langsung dengan diabetes.\n"
            "2. JIKA USER BERTANYA di luar topik tersebut (seperti masalah seksologi umum, reproduksi non-metabolik, programming, "
            "politik, gosip, atau topik kasual lainnya), Anda WAJIB MENOLAK secara halus dengan menyatakan bahwa keahlian Anda "
            "hanya terbatas pada edukasi pencegahan diabetes dan kesehatan metabolik.\n\n"
            "ATURAN MERESPONS KETAT:\n"
            "1. DILARANG KERAS menulis kalimat basa-basi di awal seperti 'Halo!', 'Terima kasih atas pertanyaannya', atau sejenisnya. LANGSUNG ke inti jawaban.\n"
            "2. Gunakan Bahasa Indonesia yang bersih, formal, dan mudah dipahami.\n"
            "3. Gunakan Markdown tebal (bold) untuk poin penting dan bullet points (-) jika memberikan rekomendasi (maksimal 3 poin pendek).\n"
            "4. JAWAB SECARA UTUH DAN SELESAIKAN KALIMAT HINGGA TUNTAS.\n"
            "5. Baris terakhir WAJIB ditutup dengan medical disclaimer singkat dan kalimat tanya: 'Ada lagi yang bisa saya bantu?'"
        )

        gemini_model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=system_instruction
        )

        generation_config = genai.types.GenerationConfig(
            temperature=0.1,        # Menurunkan suhu ke 0.1 agar AI sangat patuh pada rule guardrail dan tidak kreatif ngaco
            max_output_tokens=1000
        )

        response = gemini_model.generate_content(
            contents=user_input.message,
            generation_config=generation_config
        )

        return {
            "status_code": 200,
            "ai_response": response.text.strip()
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Gagal memproses pengiriman token dialog asisten AI: {str(e)}"
        )

# 9. RUNNER APP LOCAL SERVICE DEVELOPMENT
if __name__ == "__main__":
    import uvicorn
    print("\n[INFO] Menjalankan Infrastruktur API DiaBeat AI Secara Lokal...")
    print("[INFO] Silakan akses tautan dokumentasi lokal: http://localhost:8000/docs\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
