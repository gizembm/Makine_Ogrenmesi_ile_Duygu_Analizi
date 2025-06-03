from google.colab import files
uploaded = files.upload()

import pandas as pd

# Excel dosyasını oku (Dosya adını güncelle)
df = pd.read_excel("yeniverisetidenemesi.xlsx")

# 'Etiket' sütunundaki benzersiz değerleri bul
unique_values = df["Etiket"].unique()

# Kaç farklı etiket olduğunu yazdır
print(f"Benzersiz etiket sayısı: {len(unique_values)}")

# İsteğe bağlı: Benzersiz etiketleri yazdır
print("Benzersiz etiketler:", unique_values)

# "Etiket" sütunundaki benzersiz değerleri say
unique_count = df["Etiket"].nunique()

print(f"Benzersiz etiket sayısı: {unique_count}")

# "Etiket" sütunundaki her bir benzersiz değerin kaç kez geçtiğini say
etiket_sayilari = df["Etiket"].value_counts()

# Sonuçları yazdır
for etiket, sayi in etiket_sayilari.items():
    print(f"{etiket}: {sayi}")

# Toplam satır sayısını al (boş satırlar dahil)
toplam_satir = df.shape[0]

print(f"Excel dosyasında toplam {toplam_satir} satır var.")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Veri setini oku
file_path = "yeniverisetidenemesi.xlsx"
df = pd.read_excel(file_path)

# Etiketleri sayılara çevir
label_map = {"Olumlu": 0, "Olumsuz": 1, "Tarafsız": 2, "Spam": 3}
df["label"] = df["Etiket"].map(label_map)

# Eğitim ve test setine ayır
X_train, X_test, y_train, y_test = train_test_split(df["Yorum"], df["label"], test_size=0.2, random_state=42)

# TF-IDF vektörleştirme
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Modeli eğit
model = LogisticRegression(max_iter=200, multi_class="multinomial", solver="lbfgs")
model.fit(X_train_tfidf, y_train)

# Modeli ve vektörizeri kaydet
joblib.dump(model, "logistic_regression_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
print("Model ve TF-IDF vectorizer başarıyla kaydedildi!")


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import numpy as np

# Modelin tahmin yapması
y_pred = model.predict(X_test_tfidf)

# Performans metriklerini yazdır
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix hesapla
cm = confusion_matrix(y_test, y_pred)

# Her sınıfın doğruluğunu hesapla
class_accuracies = cm.diagonal() / cm.sum(axis=1)  # Diagonal doğru tahminler, satır toplamı ise tüm örnekler

# Ortalama doğruluğu hesapla
average_accuracy = np.mean(class_accuracies)
print(f"Ortalama Doğruluk: {average_accuracy * 100:.2f}%")

# Classification report'u al ve yüzde formatında yazdır
report = classification_report(y_test, y_pred, target_names=["Olumlu", "Olumsuz", "Tarafsız", "Spam"], output_dict=True)

# Başlık satırını yazdır
print("\nSınıf\tPrecision (%)\tRecall (%)\tF1-Score (%)")

# Sınıf raporlarını yan yana yazdır
for label, metrics in report.items():
    if label != 'accuracy':  # accuracy satırını atla
        print(f"{label}\t{metrics['precision'] * 100:.2f}%\t\t{metrics['recall'] * 100:.2f}%\t\t{metrics['f1-score'] * 100:.2f}%")

# Makro ve ağırlıklı ortalamaları da yan yana yazdır
print("\nMakro Ortalama:")
print(f"Precision: {report['macro avg']['precision'] * 100:.2f}%\tRecall: {report['macro avg']['recall'] * 100:.2f}%\tF1-Score: {report['macro avg']['f1-score'] * 100:.2f}%")

print("\nAğırlıklı Ortalama:")
print(f"Precision: {report['weighted avg']['precision'] * 100:.2f}%\tRecall: {report['weighted avg']['recall'] * 100:.2f}%\tF1-Score: {report['weighted avg']['f1-score'] * 100:.2f}%")

# Modeli ve vektörizeri kaydet
joblib.dump(model, "logistic_regression_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
print("\nModel ve TF-IDF vectorizer başarıyla kaydedildi!")

# Modeli yükle
model = joblib.load("logistic_regression_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Tahmin yapma fonksiyonu
def predict_sentiment(text):
    text_tfidf = vectorizer.transform([text])
    prediction = model.predict(text_tfidf)[0]
    return {0: "Olumlu", 1: "Olumsuz", 2: "Tarafsız", 3: "Spam"}[prediction]

# Örnek tahminler
print(predict_sentiment("isıklandırma, renklendirme kötü görünüyor ama hoşuma gitti"))
print(predict_sentiment("bu açılar oldukça salakça"))
print(predict_sentiment("açılar salakça çıkmiş"))
print(predict_sentiment("bu açılar salakça"))
print(predict_sentiment("bu açılar aptalca"))

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Test verisiyle tahmin yap
y_pred = model.predict(X_test_tfidf)

# Karışıklık matrisi
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Olumlu", "Olumsuz", "Tarafsız", "Spam"])
disp.plot(cmap=plt.cm.Blues)
plt.title("Logistic Regrasyon Karışıklık Matrisi")
plt.show()

# Sınıflandırma raporu
print("Sınıflandırma Raporu:\n", classification_report(y_test, y_pred))

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Pipeline: Metin verisini TF-IDF ile dönüştürüp modeli eğitmek için
pipeline = make_pipeline(TfidfVectorizer(), MultinomialNB())

# 5 katlı Stratified K-Fold tanımla
kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Cross-validation ile doğruluk skorlarını hesapla
scores = cross_val_score(pipeline, df["Yorum"], df["label"], cv=kf, scoring="accuracy")

# Sonuçları yazdır
print(f"Her fold için doğruluk skorları: {scores}")
print(f"Ortalama doğruluk: {scores.mean():.2f}%")
print(f"Standart sapma: {scores.std():.2f}%")
