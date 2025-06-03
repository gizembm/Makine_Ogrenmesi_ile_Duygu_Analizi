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

## 📷 Ekran Görüntüleri

### 🏠 Ana Sayfa
Kullanıcının sisteme giriş yapmadan önce karşılaştığı sayfa.

![image](https://github.com/user-attachments/assets/d0bc519d-9acc-4fa4-bc4e-516522da9d51)


---
### 🔐 Ben Kimim Ekranı
Resimleri çeken kişi hakkında kısa bir bilgi.

![image](https://github.com/user-attachments/assets/0f00e50d-a1c8-4b6e-ad66-19b3241101bf)


---

### 🔐 Giriş Yap Ekranı
Kullanıcının e-posta ve şifre bilgileriyle giriş yaptığı ekran.

![image](https://github.com/user-attachments/assets/026d036b-76be-425f-9567-a7abd14ccee7)


---
### 🔐 Kayıt Ol Ekranı
Kullanıcının e-posta ve şifre bilgileriyle Kayıt olduğu ekran.

![image](https://github.com/user-attachments/assets/0aa565a0-6b5b-48f9-bd17-fa1d49f7aff8)


---
### 🔐 İletişim Ekranı
Kullanıcının herhangi bir sıkıntı ya da öneri bir fikileri olduğunda iletişime geçebilecekleri ekran.

![image](https://github.com/user-attachments/assets/1cedac64-28f2-4230-8cee-fcfc2bb9b67b)


---

### 🖼️ Görsel Detay ve Yorum Yapma
Kullanıcının görsellere yorum yapabildiği ve analiz sonuçlarını görebildiği ekran.

![Yorum Ekleme](![image](https://github.com/user-attachments/assets/0dded22e-d3e6-487f-b5e7-6be2f98681ae))

---

### ⚠️ Spam Uyarısı
Spam içerik algılandığında sistemin verdiği uyarı.

![image](https://github.com/user-attachments/assets/9e502367-9bf8-4389-a85b-2d568c61b8fd)


---

