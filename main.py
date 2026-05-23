from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import tensorflow as tf
import numpy as np
import joblib
import logging
import os

# 1. PERBAIKAN LOGGING: Menghapus spasi dan karakter yang bikin ValueError
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="DiaBeat AI API",
    description="API Prediksi Diabetes menggunakan Deep Learning",
    version="1.2.3"
)

# 2. Load Model dan Scaler
MODEL_PATH = "baru/diabeat_model_production(v1.2).keras"
SCALER_PATH = "baru/scaler.pkl"

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    logger.info("--- [STATUS] Model dan Scaler berhasil dimuat! ---")
except Exception as e:
    logger.error(f"Gagal memuat file: {e}")

class PatientData(BaseModel):
    features: list = Field(
        ..., 
        example=[1, 45, 1, 0, 0, 125.5, 80.0, 20.0, 85.0, 28.4, 190.0, 0.45, 1, 0]
    )

@app.get("/", tags=["Status"])
def read_root():
    return {"message": "DiaBeat AI API is Online!", "documentation": "/docs"}

@app.post("/predict", tags=["Prediction"])
def predict(data: PatientData):
    try:
        # Konversi ke array 2D dengan float32 agar sinkron dengan TensorFlow
        input_features = np.array([data.features], dtype=np.float32)
        
        # 1. Scaling
        scaled_features = scaler.transform(input_features)
        logger.info(f"Inference request received. Scaled features: {scaled_features.tolist()}")

        # 2. Prediksi Menggunakan __call__ (Lebih presisi untuk nilai ekstrem)
        # Kita pakai model(x) bukan model.predict(x) buat dapet nilai mentah yang lebih jeli
        prediction = model(scaled_features, training=False)
        raw_probability = float(prediction.numpy()[0][0])
        
        # 3. FORMATTING: Trik agar tetap muncul 1.00 atau 0.00 di JSON
        # Kita kembalikan sebagai STRING agar .00 nya tidak dipangkas sistem JSON
        formatted_prob = "{:.2f}".format(raw_probability)
        
        label = "Diabetic" if raw_probability >= 0.5 else "Non-diabetic"
        logger.info(f"Result: {label} | Prob: {formatted_prob}")

        return {
            "prediction": label,
            "probability": formatted_prob # Ini akan jadi "1.00" atau "0.00"
        }
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Inference Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)