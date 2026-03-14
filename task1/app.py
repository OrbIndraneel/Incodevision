from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# ===== PUT YOUR DATASET PATH HERE =====
DATASET_PATH = "D:\INDRANEEL\CODINGDEX\College\intern\dataintern.txt"

questions = []
answers = []

# Load dataset
with open(DATASET_PATH, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            questions.append(parts[0].lower())
            answers.append(parts[1])

print("Dataset loaded:", len(questions), "conversations")

# Create TF-IDF model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)


def chatbot_response(user_input):

    user_input = user_input.lower()

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, X)

    best_match_index = similarity.argmax()

    score = similarity[0][best_match_index]

    if score > 0.3:
        return answers[best_match_index]
    else:
        return "Sorry, I don't understand that."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_response():

    data = request.get_json()

    user_input = data["message"]

    response = chatbot_response(user_input)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)