from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Modeli ve TF-IDF vectorizer'ı yükle
model = joblib.load("logistic_regression_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Etiket haritası
label_map = {0: "Olumlu", 1: "Olumsuz", 2: "Tarafsız", 3: "Spam"}


# Ana sayfa için route
@app.route("/")
def home():
    return "Flask API çalışıyor! Duygu analizi yapmak için /analyze endpoint'ini kullanın."


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # JSON formatında gelen veriyi al
        data = request.get_json()
        comment = data.get("comment", "")

        if not comment:
            return jsonify({"error": "Yorum verisi eksik!"}), 400

        # Yorumu TF-IDF formatına dönüştür
        yorum_tfidf = vectorizer.transform([comment])

        # Model ile tahmin yap
        prediction = model.predict(yorum_tfidf)[0]

        # Sonucu JSON olarak döndür
        return jsonify({"comment": comment, "prediction": label_map[prediction]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)