# Gunakan image Python resmi
FROM python:3.11

# Buat user baru agar aman (standar Hugging Face)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:${PATH}"

# Set direktori kerja
WORKDIR /app

# Copy requirements dan install library
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy semua file project (main.py, model, dan scaler langsung di sini)
COPY --chown=user . .

# Jalankan aplikasi menggunakan port 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]