# 📊 Makine Öğrenmesi ile Duygu Analizi Web Uygulaması

Bu proje, kullanıcıların yüklediği görsellere yapılan yorumları otomatik olarak analiz eden, duygu sınıflandırması yapan ve sonuçlara göre görsellere puan veren bir sosyal medya benzeri web uygulamasıdır.

## 📌 Proje Özeti

Bu sistemde:
- Kullanıcı yorumları Flask tabanlı bir Python API aracılığıyla alınır,
- Yorumlar ön işleme sürecinden geçirilerek analiz edilir,
- Logistic Regression, Naive Bayes, SVM ve LSTM gibi çeşitli makine öğrenmesi ve derin öğrenme algoritmaları denenmiş,
- En yüksek başarı oranını veren model seçilerek sistemde entegre edilmiştir.

## 🚀 Kullanılan Teknolojiler

- **Backend**: ASP.NET MVC5 (C#)
- **Frontend**: HTML, CSS, JavaScript, Razor View
- **Veritabanı**: MSSQL Server
- **API**: Python & Flask RESTful API
- **Makine Öğrenmesi**: Scikit-learn, NLTK, Keras
- **Modelleme**: Logistic Regression, Naive Bayes, SVM, LSTM

## 🧠 Model Performans Karşılaştırması

| Model                | Doğruluk (%) |
|----------------------|--------------|
| Naive Bayes          | 86.32        |
| SVM                  | 90.53        |
| LSTM                 | 89.47        |
| Logistic Regression  | **91.11**    |

> Projede Logistic Regression modeli en yüksek doğruluğu sağladığı için tercih edilmiştir.

## 🖼️ Özellikler

- Kullanıcı kayıt ve giriş sistemi
- Görsel yükleme ve yorum yapma
- Anlık duygu analizi (Olumlu, Olumsuz, Tarafsız, Spam)
- Görsellere yorumlara göre otomatik yıldız puanlama
- Spam yorum filtreleme ve uyarı sistemi
- İletişim formu ve admin paneli

## 🗃️ Veritabanı Yapısı

Veritabanı aşağıdaki ana tabloları içerir:
- `Kullanicilar`
- `Resimler`
- `Yorumlar`
- `YorumAnaliz`
- `Iletisim`

## 🔁 API Entegrasyonu

- Yorum, ASP.NET MVC tarafından JSON formatında Flask API'ye gönderilir.
- Python tarafındaki model, yorumun duygu etiketini belirler.
- Etiketlenen yorumlar MSSQL veritabanına kaydedilir.
- Kullanıcı, yorumunun sonucunu arayüzde görür.

## 📂 Veri Seti

- `karisik_yorum_veriseti.xlsx`: Olumlu, Olumsuz, Tarafsız, Spam olarak etiketlenmiş Türkçe yorumlardan oluşur.
- Kaynak: [IMDB Turkish Dataset](https://github.com/fatihilhan/IMDB-Turkish-Dataset), [Sentiment140](https://github.com/kazanova/sentiment140)

## 📷 Uygulama Görselleri

- Ana Sayfa
- Kayıt / Giriş Ekranı
- Görsel Detay ve Yorum Ekleme
- Duygu Analizi Sonuçları
- Spam Yorum Uyarı Sistemi

## 👨‍💻 Katılımcılar

- Dilara Öztürk
- Yasemin Kılıç
- Gizem Efe
- Hilal Şarkışla
- Elif Sude Ünal

## 📜 Lisans

Bu proje akademik bir çalışmadır. Ticari amaçlarla kullanılması durumunda lütfen geliştiricilere ulaşınız.

---

