import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

# --- 1. MODELİ YÜKLEME ---
model_path = 'regresyon_modeli.pkl'

# Modeli yüklemeyi dene, yoksa hata mesajı ver
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("Model başarıyla yüklendi.")
except FileNotFoundError:
    model = None
    print("HATA: 'regresyon_modeli.pkl' bulunamadı. Lütfen dosyanın aynı klasörde olduğundan emin olun.")

# --- 2. GİRİŞ ÖZELLİKLERİ (Backward Elimination Sonrası Kalan 9 Öznitelik) ---
# Bu sıralama, model eğitimi sırasındaki sıralama ile AYNI olmalıdır.
FINAL_FEATURES = ['CRIM', 'CHAS', 'NOX', 'RM', 'DIS', 'RAD', 'PTRATIO', 'B', 'LSTAT']

@app.route('/')
def home():
    """Ana sayfayı (formu) gösterir."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Formdan verileri alır ve tahmin yapar."""
    
    if not model:
        return render_template('index.html', prediction_text="HATA: Model dosyası yüklenemedi.")

    try:
        # Formdan gelen verileri listeye çekme ve float'a çevirme
        feature_values = []
        for feature in FINAL_FEATURES:
            val = request.form.get(feature)
            feature_values.append(float(val))
        
        # Modelin beklediği format olan DataFrame'e çevirme
        features_df = pd.DataFrame([feature_values], columns=FINAL_FEATURES)

        # Tahmin Yapma
        prediction = model.predict(features_df)
        
        # Sonucu yuvarlama (Örn: 24.56)
        output = round(prediction[0], 2)

        # Sonucu ekrana gönderme
        return render_template('index.html', prediction_text=f'Tahmin Edilen Ev Fiyatı: ${output}0 (MEDV)')

    except Exception as e:
        return render_template('index.html', prediction_text=f"Hata oluştu: {e}. Lütfen tüm alanlara sayı girdiğinizden emin olun.")

if __name__ == "__main__":
    app.run(debug=True)