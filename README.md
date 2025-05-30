# Full Data Science Pipeline Project

Bu proje, uçtan uca bir veri bilimi sürecini simüle eden, orta seviye bir projedir.  
Gerçek veri yerine **yapay (synthetic)** olarak oluşturulmuş, güvenli ve paylaşılabilir veri setleri kullanılmıştır.

---

# Amaç

- Veri temizleme, özellik mühendisliği, gözetimli ve gözetimsiz öğrenme
- A/B testi simülasyonu ve istatistiksel çıkarım
- Model değerlendirme, izleme ve dağıtım stratejileri
- Görselleştirme ve temel mobil analitik kavramlarının uygulanması

---

# Proje Yapısı

```bash
full_data_science_project/
│
├── data/
│   ├── user_data.csv               # Kullanıcı verisi (yapay)
│   └── model_data.csv              # Classification verisi
│
├── scripts/
│   ├── data_wrangling.py
│   ├── feature_engineering.py
│   ├── supervised_learning.py
│   ├── unsupervised_learning.py
│   ├── ab_testing.py
│   ├── model_evaluation.py
│   ├── model_monitoring.py
│   └── visualization_examples.py
│
├── mobile_analytics_concepts.md   # ROAS, retention, funnel analizi
├── sql_queries.sql                # Segmentasyon ve retention sorguları
├── deployment_pipeline.txt        # Batch / API dağıtım açıklaması
├── LICENSE
├── .gitignore
└── README.md
