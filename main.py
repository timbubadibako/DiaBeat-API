from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import tensorflow as tf
import numpy as np
import joblib

# 1. Inisialisasi FastAPI dengan Metadata
app = FastAPI(
    title="DiaBeat AI API",
    description="API Prediksi Diabetes menggunakan Deep Learning (Functional API)",
    version="1.2.1"
)

# 2. Load Model dan Scaler
# Path directory tetap sesuai permintaanmu
try:
    model = tf.keras.models.load_model("baru/diabeat_model_production(v1.2).keras")
    scaler = joblib.load("baru/scaler.pkl")
    print("[SUCCESS] Model dan Scaler berhasil dimuat!")
except Exception as e:
    print(f"[ERROR] Gagal memuat file: {e}")

# 3. Struktur Data Input (Format List)
class PatientData(BaseModel):
    # Field example ini yang bikin di Swagger UI /docs muncul angkanya otomatis bray
    features: list = Field(
        ..., 
        example=[1, 45, 1, 0, 0, 125.5, 80.0, 20.0, 85.0, 28.4, 190.0, 0.45, 1, 0],
        description="List angka fitur (Urutan: Gender, Age, Activity, Smoking, Alcohol, Glucose, BP, Thickness, Insulin, BMI, Chol, Pedigree, Family, Hypertension)"
    )

@app.get("/", tags=["Status"])
def read_root():
    return {"message": "DiaBeat AI API is Online!", "documentation": "/docs"}

@app.post("/predict", tags=["Prediction"])
def predict(data: PatientData):
    try:
        # Konversi input list ke format yang dipahami model (2D Array)
        input_features = np.array([data.features])

        # 1. Scaling data (Wajib!)
        # Jika error di sini, berarti jumlah angka di list 'features' nggak sama dengan pas training
        scaled_features = scaler.transform(input_features)

        # 2. Prediksi (verbose=0 biar terminal anteng)
        prediction = model.predict(scaled_features, verbose=0)
        probability = float(prediction[0][0])
        
        # 3. Output JSON sesuai permintaan Backend
        return {
            "prediction": "Diabetic" if probability >= 0.5 else "Non-diabetic",
            "probability": round(probability, 2)
        }
        
    except Exception as e:
        # Kalau jumlah fitur beda, bakal ketauan di sini
        raise HTTPException(status_code=500, detail=f"Inference Error: {str(e)}")

# 4. Menjalankan Server (Gunakan: python main.py)
if __name__ == "__main__":
    import uvicorn
    print("\n[INFO] Menjalankan Server DiaBeat AI...")
    print("[INFO] Buka dokumentasi untuk test: http://localhost:8000/docs\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)