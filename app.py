from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    symptom = request.form.get("symptom", "").strip().lower()

    health_info = {
        "headache": "Headaches can have many causes, including stress, dehydration, or lack of sleep.",
        "fever": "Fever can occur with infections and other conditions. Monitor your temperature.",
        "cough": "A cough can have several causes, such as a cold, allergy, or respiratory infection.",
        "cold": "Common cold symptoms may include a runny nose, sneezing, and sore throat.",
        "stomach pain": "Stomach pain can have many causes. Persistent or severe pain should be evaluated by a healthcare professional."
    }

    result = health_info.get(
        symptom,
        "No information available for this symptom. Please consult a qualified healthcare professional."
    )

    return f"""
    <html>
        <head>
            <title>Healthcare Result</title>
        </head>
        <body>
            <h1>🏥 Healthcare Information</h1>
            <p><strong>Symptom:</strong> {symptom}</p>
            <p><strong>Information:</strong> {result}</p>
            <a href="/">← Check another symptom</a>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)