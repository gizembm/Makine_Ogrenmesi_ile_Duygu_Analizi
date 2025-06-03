from google.colab import files
uploaded = files.upload()

file_path = "+1200veriseti.xlsx"

import pandas as pd
import re

# Excel dosyasını oku
file_path = "yeniverisetidenemesi.xlsx"
df = pd.read_excel(file_path)

# İlk 5 satırı göster
print(df.tail())

# Noktalama işaretlerini ve gereksiz boşlukları kaldır
def clean_text(text):
    if isinstance(text, str):  # Sadece string değerleri işle
        # Noktalama işaretlerini kaldır
        text = re.sub(r'[^\w\s]', '', text)
        # Birden fazla boşluğu tek boşluğa dönüştür
        text = re.sub(r'\s+', ' ', text)
        # Baştaki ve sondaki boşlukları kaldır
        text = text.strip()
    return text

# Tüm metin sütunlarına temizleme işlemini uygula
df["Yorum"] = df["Yorum"].apply(clean_text)

# NaN değerlerini kontrol et
print(df.isnull().sum())

# Etiketleri sayılara çevir
label_map = {"Olumlu": 0, "Olumsuz": 1, "Tarafsız": 2, "Spam": 3}
df["label"] = df["Etiket"].map(label_map)

from sklearn.model_selection import train_test_split

# Eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(df["Yorum"], df["label"], test_size=0.2, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF vektörleştirici
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

# Naive Bayes modelini tanımla ve eğit
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)

# Test verisiyle tahmin yap
y_pred_nb = nb_model.predict(X_test_tfidf)

# Model performansını değerlendir
accuracy = accuracy_score(y_test, y_pred_nb)
print(f"Naive Bayes Doğruluk Oranı: {accuracy * 100:.2f}%")

# Sınıflandırma raporunu al
report = classification_report(y_test, y_pred_nb, target_names=["Olumlu", "Olumsuz", "Tarafsız", "Spam"], output_dict=True)

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

import joblib

# Naive Bayes modelini ve vektörleştiriciyi kaydet
joblib.dump(nb_model, "naive_bayes_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

from google.colab import files

files.download("naive_bayes_model.pkl")
files.download("tfidf_vectorizer.pkl")

def duygu_analizi_yap_naive_bayes_detayli(cumle):
    """
    Verilen cümlenin duygu analizini Naive Bayes modeli ile yapar ve tahmin olasılıklarını döndürür.

    Parametreler:
    cumle (str): Analiz edilecek cümle.

    Returns:
    dict: Tahmin edilen duygu ve sınıf olasılıkları.
    """
    # Naive Bayes modelini ve vektörleştiriciyi yükle
    nb_model = joblib.load("naive_bayes_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")

    # Cümleyi TF-IDF vektörüne dönüştür
    cumle_tfidf = vectorizer.transform([cumle])

    # Tahmin yap
    tahmin = nb_model.predict(cumle_tfidf)
    tahmin_olasiliklari = nb_model.predict_proba(cumle_tfidf)

    # Tahmini etikete dönüştür
    label_map = {0: "Olumlu", 1: "Olumsuz", 2: "Tarafsız", 3: "Spam"}
    tahmin_etiketi = label_map[tahmin[0]]

    # Sınıf olasılıklarını hazırla
    olasiliklar = {
        "Olumlu": tahmin_olasiliklari[0][0],
        "Olumsuz": tahmin_olasiliklari[0][1],
        "Tarafsız": tahmin_olasiliklari[0][2],
        "Spam": tahmin_olasiliklari[0][3]
    }

    return {
        "tahmin": tahmin_etiketi,
        "olasiliklar": olasiliklar
    }

cumle = "çok mükemmel değil ama fena sayılmaz"
sonuc = duygu_analizi_yap_naive_bayes_detayli(cumle)
print(f"Cümle: '{cumle}' -> Tahmin: {sonuc['tahmin']}")
print("Olasılıklar:", sonuc["olasiliklar"])

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Karışıklık matrisi
cm = confusion_matrix(y_test, y_pred_nb)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Olumlu", "Olumsuz", "Tarafsız", "Spam"])
disp.plot(cmap=plt.cm.Blues)
plt.title("Naive Bayes Karışıklık Matrisi")
plt.show()

