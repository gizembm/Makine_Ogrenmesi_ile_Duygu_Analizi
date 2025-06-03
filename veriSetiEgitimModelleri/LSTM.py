from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.regularizers import l1_l2
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping

# Veri setini yükle
file_path = "yeniverisetidenemesi.xlsx"
df = pd.read_excel(file_path)

# Metin temizleme fonksiyonu
def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'[^\w\s]', '', text)  # Noktalama işaretlerini kaldır
        text = re.sub(r'\s+', ' ', text)      # Birden fazla boşluğu tek boşluğa dönüştür
        text = text.strip()                   # Baştaki ve sondaki boşlukları kaldır
    return text

# Temizleme işlemini uygula
df["Yorum"] = df["Yorum"].apply(clean_text)

# NaN değerlerini temizle
df = df.dropna()

# Etiketleri sayısallaştır
label_map = {"Olumlu": 0, "Olumsuz": 1, "Tarafsız": 2, "Spam": 3}
df["label"] = df["Etiket"].map(label_map)
labels = df["label"].values

# Tokenizer'ı tanımla ve metinleri tokenize et
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(df["Yorum"])
sequences = tokenizer.texts_to_sequences(df["Yorum"])

# Padding işlemi
max_len = 100  # Maksimum dizi uzunluğu
X = pad_sequences(sequences, maxlen=max_len)

# Etiketleri one-hot encoding yap
y = to_categorical(labels, num_classes=4)

# Eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LSTM modelini tanımla
model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=128, input_length=max_len))
model.add(LSTM(128, dropout=0.3, recurrent_dropout=0.3, kernel_regularizer=l1_l2(l1=0.0001, l2=0.0001)))
model.add(Dense(64, activation="relu", kernel_regularizer=l1_l2(l1=0.0001, l2=0.0001)))
model.add(Dropout(0.5))
model.add(Dense(4, activation="softmax"))

# Modeli derle
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Erken durdurma callback'i
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Modeli eğit
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=64,
    validation_data=(X_test, y_test),
    callbacks=[early_stopping]
)


from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Model ile test seti üzerinde tahmin yap
y_pred = model.predict(X_test)

# Tahminleri en yüksek olasılık sınıfına dönüştür
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

# Confusion Matrix'i oluştur
cm = confusion_matrix(y_true_classes, y_pred_classes)

# Confusion Matrix'i görselleştir
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Olumlu", "Olumsuz", "Tarafsız", "Spam"], yticklabels=["Olumlu", "Olumsuz", "Tarafsız", "Spam"])
plt.xlabel("Tahmin Edilen Etiket")
plt.ylabel("Gerçek Etiket")
plt.title("LSTM Karışıklık Matrisi")
plt.show()



import matplotlib.pyplot as plt

# Eğitim ve doğrulama kaybını çiz
plt.plot(history.history["loss"], label="Eğitim Kaybı")
plt.plot(history.history["val_loss"], label="Doğrulama Kaybı")
plt.title("Eğitim ve Doğrulama Kaybı")
plt.xlabel("Epoch")
plt.ylabel("Kayıp")
plt.legend()
plt.show()

# Eğitim ve doğrulama doğruluğunu çiz
plt.plot(history.history["accuracy"], label="Eğitim Doğruluğu")
plt.plot(history.history["val_accuracy"], label="Doğrulama Doğruluğu")
plt.title("Eğitim ve Doğrulama Doğruluğu")
plt.xlabel("Epoch")
plt.ylabel("Doğruluk")
plt.legend()
plt.show()

from sklearn.metrics import classification_report, accuracy_score
import numpy as np

# Test veri kümesi için tahminleri al
y_pred_probs = model.predict(X_test)  # Olasılıklar
y_pred = np.argmax(y_pred_probs, axis=1)  # En yüksek olasılığa sahip sınıfı al
y_true = np.argmax(y_test, axis=1)  # Gerçek etiketleri çöz

# Precision, Recall, F1-score ve Accuracy hesapla
report = classification_report(y_true, y_pred, target_names=["Olumlu", "Olumsuz", "Tarafsız", "Spam"], output_dict=True)

# Tüm etiketler için yüzdelik metrikleri yazdır
for label in ["Olumlu", "Olumsuz", "Tarafsız", "Spam"]:
    precision = report[label]["precision"] * 100
    recall = report[label]["recall"] * 100
    f1 = report[label]["f1-score"] * 100
    print(f"{label} -> Precision: %{precision:.2f}, Recall: %{recall:.2f}, F1-Score: %{f1:.2f}")

# Ortalama doğruluk oranı
accuracy = accuracy_score(y_true, y_pred) * 100
print(f"Genel Doğruluk (Accuracy): %{accuracy:.2f}")



# Modeli kaydet
model.save("lstm_duygu_analizi_modeli.h5")

# Tokenizer'ı kaydet
import pickle
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

    from google.colab import files

    files.download("lstm_duygu_analizi_modeli.h5")
    files.download("tokenizer.pkl")