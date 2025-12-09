# 📈 Proje 3: Çoklu Doğrusal Regresyon ve Flask Web Arayüzü

Bu proje, Boston Ev Fiyatları veri seti üzerinde Çoklu Doğrusal Regresyon modeli kurulmasını, istatistiksel öznitelik seçimi yapılmasını ve modelin Flask ile web tabanlı bir GUI ile sunulmasını içerir.

---

## 📝 Dökümantasyon ve İçerik

* **regresyon_projesi.ipynb:** Veri ön işleme, Backward Elimination ve model metrik analizlerinin yapıldığı ana analiz dosyasıdır.
* **app.py:** Flask uygulamasının çekirdek kodudur (Modeli yükler ve tahmini yapar).
* **regresyon_modeli.pkl:** Scikit-learn ile eğitilmiş olan final model ağırlıklarıdır.
* **templates/index.html:** Kullanıcıdan 9 özniteliği alan basit ve işlevsel web arayüzü formudur (GUI).

---

## Analiz ve Öznitelik Seçimi

# 1. Backward Elimination Sonuçları

Öznitelik sayısını maksimum 10'a indirmek için p-değeri analizi yapılmış ve en anlamlı öznitelikler seçilmiştir.

* **Kalan 9 Öznitelik:** CRIM, CHAS, NOX, RM, DIS, RAD, PTRATIO, B, LSTAT
* **Elenen Öznitelikler:** INDUS, AGE, ZN, TAX
* **Açıklama:** Bu 9 öznitelik, fiyat tahmini üzerinde istatistiksel olarak en anlamlı katkıyı sağlamaktadır.

# 2. Model Başarısı (Test Seti Metrikleri)

Final modelin performansı:

* **R-Kare (R²):** 0.6349
    * **Yorum:** Model, ev fiyatındaki değişkenliğin yaklaşık %63.49'unu açıklamaktadır.
* **MAE (Ortalama Mutlak Hata):** 3.3377
    * **Yorum:** Tahminler, gerçek ev fiyatından ortalama 3.3377 birim sapmaktadır.
* **MSE (Ortalama Karesel Hata):** 26.7713

---

# Flask Web Uygulamasının Çalıştırılması

Web arayüzü, hocanın istediği basit, işlevsel ve kullanıcıdan tüm giriş özelliklerini alan form yapısını sağlamaktadır.

# Kurulum

1.  `Proje_3_Regresyon_Flask` klasörüne gidin.
2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install flask pandas scikit-learn
    ```

# Çalıştırma

1.  Terminalde uygulamayı başlatın:
    ```bash
    python app.py
    ```
2.  Tarayıcınızda çıkan linki açın: **`http://127.0.0.1:5000/`**

# Kullanım

Arayüzde 9 öznitelik için değerler girilir ve **"Fiyatı Tahmin Et"** butonuna basıldığında, model tahmin sonucunu ($1000$ cinsinden MEDV) ekranda gösterir.
