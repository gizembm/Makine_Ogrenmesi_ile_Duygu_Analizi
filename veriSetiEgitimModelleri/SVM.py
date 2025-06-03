from google.colab import files
uploaded = files.upload()

file_path = "+1200veriseti.xlsx"

import pandas as pd
import re
from snowballstemmer import TurkishStemmer

# Türkçe stopwords listesi
turkce_stopwords = ["acaba", "ama", "ancak", "aslında", "az", "bazı", "belki", "biri", "birkaç", "birşey", "biz", "çok", "çünkü", "da", "daha", "de", "defa", "diye", "eğer", "en", "gibi", "hem", "hep", "hepsi", "her", "hiç", "için", "ile", "ise", "kez", "ki", "kim", "mı", "mu", "mü", "nasıl", "ne", "neden", "nerde", "nerede", "nereye", "niçin", "niye", "o", "sanki", "şey", "siz", "şu", "tüm", "ve", "veya", "ya", "yani"]

# Türkçe stemmer
stemmer = TurkishStemmer()

# Metin temizleme ve kök bulma fonksiyonu
def preprocess_text(text):
    if isinstance(text, str):
        # Noktalama işaretlerini kaldır
        text = re.sub(r'[^\w\sğüşıöçĞÜŞİÖÇ]', '', text)
        # Birden fazla boşluğu tek boşluğa dönüştür
        text = re.sub(r'\s+', ' ', text)
        # Baştaki ve sondaki boşlukları kaldır
        text = text.strip()
        # Kelimeleri köklerine ayır ve stopwords'leri kaldır
        words = text.split()
        stemmed_words = [stemmer.stemWord(word) for word in words if word not in turkce_stopwords]
        text = " ".join(stemmed_words)
    return text

# Veri setini yükle
file_path = "yeniverisetidenemesi.xlsx"
df = pd.read_excel(file_path)

# Metinleri ön işleme adımlarından geçir
df["Yorum"] = df["Yorum"].apply(preprocess_text)

# NaN değerlerini kontrol et ve temizle
print(df.isnull().sum())
df = df.dropna()

# Etiketleri sayısallaştır
label_map = {"Olumlu": 0, "Olumsuz": 1, "Tarafsız": 2, "Spam": 3}
df["label"] = df["Etiket"].map(label_map)

from sklearn.model_selection import train_test_split

# Eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(df["Yorum"], df["label"], test_size=0.2, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF vektörleştirici
vectorizer = TfidfVectorizer(max_features=5000, stop_words=turkce_stopwords)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# SVM modelini tanımla ve eğit
svm_model = SVC(kernel="linear", probability=True)  # probability=True, tahmin olasılıkları için
svm_model.fit(X_train_tfidf, y_train)

# Test verisiyle tahmin yap
y_pred_svm = svm_model.predict(X_test_tfidf)

# Doğruluk oranını hesapla ve yüzdelik formatta yazdır
accuracy = accuracy_score(y_test, y_pred_svm)
print(f"SVM Doğruluk Oranı: {accuracy * 100:.2f}%")

# Sınıflandırma raporunu al ve yüzdelik formatta yazdır
report = classification_report(y_test, y_pred_svm, output_dict=True)

# Başlıkları yazdır
print("\nSınıf\tPrecision (%)\tRecall (%)\tF1-Score (%)")

# Her sınıf için precision, recall, f1-score değerlerini yan yana yazdır
for label, metrics in report.items():
    if label != 'accuracy':  # accuracy satırını atla
        print(f"{label}\t{metrics['precision'] * 100:.2f}%\t\t{metrics['recall'] * 100:.2f}%\t\t{metrics['f1-score'] * 100:.2f}%")

# Makro ve ağırlıklı ortalamaları da yan yana yazdır
print("\nMakro Ortalama:")
print(f"Precision: {report['macro avg']['precision'] * 100:.2f}%\tRecall: {report['macro avg']['recall'] * 100:.2f}%\tF1-Score: {report['macro avg']['f1-score'] * 100:.2f}%")

print("\nAğırlıklı Ortalama:")
print(f"Precision: {report['weighted avg']['precision'] * 100:.2f}%\tRecall: {report['weighted avg']['recall'] * 100:.2f}%\tF1-Score: {report['weighted avg']['f1-score'] * 100:.2f}%")


import joblib

# SVM modelini ve vektörleştiriciyi kaydet
joblib.dump(svm_model, "svm_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

from google.colab import files

files.download("svm_model.pkl")
files.download("tfidf_vectorizer.pkl")

def duygu_analizi_yap_svm_detayli(cumle):
    """
    Verilen cümlenin duygu analizini SVM modeli ile yapar ve tahmin olasılıklarını döndürür.

    Parametreler:
    cumle (str): Analiz edilecek cümle.

    Returns:
    dict: Tahmin edilen duygu ve sınıf olasılıkları.
    """
    # SVM modelini ve vektörleştiriciyi yükle
    svm_model = joblib.load("svm_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")

    # Cümleyi ön işleme adımlarından geçir
    cumle = preprocess_text(cumle)

    # Cümleyi TF-IDF vektörüne dönüştür
    cumle_tfidf = vectorizer.transform([cumle])

    # Tahmin yap
    tahmin = svm_model.predict(cumle_tfidf)
    tahmin_olasiliklari = svm_model.predict_proba(cumle_tfidf)

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

# Örnek tahmin
cumle = "resmi beğendim"
sonuc = duygu_analizi_yap_svm_detayli(cumle)
print(f"Cümle: '{cumle}' -> Tahmin: {sonuc['tahmin']}")
print("Olasılıklar:", sonuc["olasiliklar"])

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Karışıklık matrisi
cm = confusion_matrix(y_test, y_pred_svm)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Olumlu", "Olumsuz", "Tarafsız", "Spam"])
disp.plot(cmap=plt.cm.Blues)
plt.title("SVM Karışıklık Matrisi")
plt.show()

