import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset (tab separated)
data = pd.read_csv(
    "D:\INDRANEEL\CODINGDEX\College\intern\Task2\SMSSpamCollection",
    sep="\t",
    names=["label", "message"]
)

print("Dataset Loaded:", data.shape)

# Convert labels to numbers
data['label'] = data['label'].map({'ham':0, 'spam':1})

# Features and labels
X = data['message']
y = data['label']

# Vectorization
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Model evaluation
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# User input prediction
while True:

    msg = input("\nEnter message (type 'exit' to stop): ")

    if msg.lower() == "exit":
        break

    msg_vector = vectorizer.transform([msg])

    prediction = model.predict(msg_vector)[0]

    if prediction == 1:
        print("⚠️ Spam Message")
    else:
        print("✅ Not Spam")