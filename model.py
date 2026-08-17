import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("symptoms.csv")

# Input and output
X = data["symptom"]
y = data["disease"]

# Convert symptoms into numerical features
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Train the model
model = LogisticRegression()
model.fit(X_vectorized, y)


def predict_disease(symptom):
    symptom_vector = vectorizer.transform([symptom])
    prediction = model.predict(symptom_vector)

    return prediction[0]


if __name__ == "__main__":
    symptom = input("Enter symptom: ")

    result = predict_disease(symptom)

    print("Predicted condition:", result)