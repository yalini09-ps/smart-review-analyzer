from flask import Flask, render_template, request
from model import predict_disease

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    symptom = request.form.get("symptom", "").strip()

    if not symptom:
        result = "Please enter a symptom."
    else:
        result = predict_disease(symptom)

    return render_template(
        "result.html",
        symptom=symptom,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)