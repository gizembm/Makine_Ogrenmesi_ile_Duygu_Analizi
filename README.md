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

## 👨‍💻 Katılımcılar

- Dilara Öztürk
- Yasemin Kılıç
- Gizem Efe
- Hilal Şarkışla
- Elif Sude Ünal


## 📷 Uygulama Görselleri

### 🏠 Ana Sayfa  
Kullanıcının sisteme giriş yapmadan önce karşılaştığı sayfa.

<p align="left">
  <img src="https://github.com/user-attachments/assets/d0bc519d-9acc-4fa4-bc4e-516522da9d51" width="800"/>
</p>

---

### 🧑‍💼 Ben Kimim Ekranı  
Resimleri çeken kişi hakkında kısa bir bilgi.

<p align="left">
  <img src="https://github.com/user-attachments/assets/843f3ee0-256e-4b37-aaeb-097d13ac213c" width="800"/>
</p>

---

### 🔐 Giriş Yap Ekranı  
Kullanıcının e-posta ve şifre bilgileriyle giriş yaptığı ekran.

<p align="left">
  <img src="https://github.com/user-attachments/assets/566e90b5-b126-470b-bebe-15227150f9f0" width="800"/>
</p>

---

### 📝 Kayıt Ol Ekranı  
Kullanıcının e-posta ve şifre bilgileriyle kayıt olduğu ekran.

<p align="left">
  <img src="https://github.com/user-attachments/assets/a1a2e071-8024-4af5-9987-dc19bab79b40" width="800"/>
</p>

---

### 📬 İletişim Ekranı  
Kullanıcının herhangi bir sıkıntı ya da öneri fikri olduğunda iletişime geçebileceği ekran.

<p align="left">
  <img src="https://github.com/user-attachments/assets/eb0c21f5-8987-4869-92fd-71e9615a5ff7" width="800"/>
</p>

---

### 🖼️ Görsel Detay ve Yorum Yapma  
Kullanıcının görsellere yorum yapabildiği ve analiz sonuçlarını görebildiği ekran.

<p align="left">
  <img src="https://github.com/user-attachments/assets/9d77b344-e887-4d24-9702-968183436cca" width="800"/>
</p>

---

### ⚠️ Spam Uyarısı  
Spam içerik algılandığında sistemin verdiği uyarı.

<p align="left">
  <img src="https://github.com/user-attachments/assets/6d532e0f-41e5-41ab-9db1-402c3280cb46" width="800"/>
  <br><br>
  <img src="https://github.com/user-attachments/assets/a1e574a7-d489-48db-9a22-40f1ce556628" width="800"/>
</p>







---
