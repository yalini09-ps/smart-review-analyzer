from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    symptom = request.form.get("symptom")

    # Basic example response
    if symptom:
        result = f"You entered: {symptom}"
    else:
        result = "Please enter a symptom."

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)