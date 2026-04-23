from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import joblib

# 1. Inisialisasi FastAPI
app = FastAPI(title="DiaBeat AI API")

# 2. Load Model dan Scaler
try:
    # Load model deep learning
    model = tf.keras.models.load_model("diabeat_model_production.keras")
    # Load scaler untuk normalisasi data
    scaler = joblib.load("scaler.pkl")
    print("[SUCCESS] Model dan Scaler berhasil dimuat!")
except Exception as e:
    print(f"[ERROR] Gagal memuat file: {e}")

# 3. Struktur Data Input (Harus sesuai urutan dataset)
class PatientData(BaseModel):
    Gender: int
    Age: int
    Physical_Activity: int
    Smoking_Status: int
    Alcohol_Intake: int
    Glucose: float
    Blood_Pressure: float
    Skin_Thickness: float
    Insulin: float
    BMI: float
    Cholesterol: float
    Diabetes_Pedigree: float
    Family_History: int
    Hypertension: int

@app.get("/")
def read_root():
    return {"message": "DiaBeat AI API is Online!"}

@app.post("/predict")
def predict(data: PatientData):
    try:
        # Konversi JSON ke Array
        input_features = np.array([[
            data.Gender, data.Age, data.Physical_Activity, data.Smoking_Status,
            data.Alcohol_Intake, data.Glucose, data.Blood_Pressure, data.Skin_Thickness,
            data.Insulin, data.BMI, data.Cholesterol, data.Diabetes_Pedigree,
            data.Family_History, data.Hypertension
        ]])

        # Scaling data (WAJIB agar akurasi sama dengan di Colab)
        scaled_features = scaler.transform(input_features)

        # Prediksi
        prediction = model.predict(scaled_features)
        probability = float(prediction[0][0])
        
        return {
            "status": "success",
            "prediction": {
                "risk_score": round(probability * 100, 2),
                "is_diabetic": bool(probability > 0.5),
                "label": "Diabetic" if probability > 0.5 else "Non-diabetic"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))