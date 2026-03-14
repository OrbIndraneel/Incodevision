#Task 1
# 🤖 AI Chatbot using Python, Flask & NLP

This project is a **web-based AI chatbot** built using **Python, Flask, and Natural Language Processing (NLP)** techniques.
The chatbot uses a conversational **dataset stored in a TXT file** and applies **TF-IDF vectorization with cosine similarity** to generate relevant responses.

The project demonstrates how a simple dataset-driven chatbot can be converted into an interactive **web application with an attractive UI**.

---

## 🚀 Features

* 💬 Interactive web-based chatbot interface
* 📚 Uses a **conversation dataset (TXT file)**
* 🧠 NLP-based response matching using **TF-IDF & Cosine Similarity**
* 🌐 Flask-based backend server
* 🎨 Modern chat-style UI with message bubbles
* ⌨️ Supports **Enter key for sending messages**
* 🔄 Automatically scrolls to latest messages

---

## 🛠 Technologies Used

* Python
* Flask
* Scikit-learn
* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```
task1
│
├── app.py                # Flask backend server
├── dataintern.txt        # Conversation dataset
│
└── templates
      └── index.html      # Chatbot UI
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/OrbIndraneel/Incodevision.git
```

Move into the project directory:

```
cd Incodevision/task1
```

Install required dependencies:

```
pip install flask scikit-learn
```

---

## ▶️ Running the Project

Start the Flask server:

```
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. The chatbot loads a **conversation dataset** from a TXT file.
2. User input is converted into a **TF-IDF vector**.
3. The program calculates **cosine similarity** between the user input and dataset questions.
4. The chatbot returns the **most similar response** from the dataset.

---

## 📈 Future Improvements

* Add **deep learning NLP models**
* Integrate **speech-to-text chatbot**
* Store conversations in a **database**
* Deploy the chatbot on **cloud platforms**

---
#Task 2

# 📩 Spam Message Detection using Machine Learning

This project implements a **Spam Message Detection System** using **Machine Learning and Natural Language Processing (NLP)** techniques.

The model analyzes text messages and predicts whether they are **Spam or Not Spam (Ham)**. It uses the **SMS Spam Collection Dataset** and applies **TF-IDF text vectorization** along with a **Naive Bayes classifier** to perform the classification.

This project was developed as **Task-02 during my Internship at Incodevision** to understand the fundamentals of **text processing, machine learning models, and predictive systems**.

---

## 🚀 Features

* Detects whether a message is **Spam or Not Spam**
* Uses a **real-world SMS spam dataset**
* Applies **TF-IDF text vectorization**
* Uses **Naive Bayes classification algorithm**
* Allows **user input for real-time prediction**
* Evaluates model performance using **accuracy score**

---

## 🛠 Technologies Used

* Python
* Pandas
* Scikit-learn
* Natural Language Processing (NLP)

---

## 📂 Project Structure

```text
Task2
│
├── spam_detector.py      # Machine learning spam detection script
├── SMSSpamCollection     # Dataset file
└── README.md
```

---

## 📊 Dataset

The model is trained using the **SMS Spam Collection Dataset**, which contains **5,500+ SMS messages** labeled as:

* **Ham** → Legitimate message
* **Spam** → Unwanted or promotional message

Example:

```
ham   Hey, are we meeting tomorrow?
spam  Congratulations! You have won a free prize
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/OrbIndraneel/Incodevision.git
```

Navigate to the Task2 folder:

```bash
cd Incodevision/Task2
```

Install required dependencies:

```bash
pip install pandas scikit-learn
```

---

## ▶️ Running the Project

Run the spam detection program:

```bash
python spam_detector.py
```

Then enter any message to test whether it is spam.

Example:

```
Enter message: Congratulations you won a free iPhone
⚠️ Spam Message

Enter message: Let's meet tomorrow
✅ Not Spam
```

---

## 🧠 How It Works

1. The dataset is loaded and labeled messages are processed.
2. Text messages are converted into numerical features using **TF-IDF Vectorization**.
3. The dataset is split into **training and testing sets**.
4. A **Naive Bayes classifier** is trained on the training data.
5. The model predicts whether a new message is **Spam or Not Spam**.

---

## 📈 Future Improvements

* Deploy as a **web application using Flask**
* Add **deep learning models (LSTM / Transformers)**
* Improve accuracy with **advanced preprocessing**
* Integrate with **email or messaging systems**

---

## 👨‍💻 Author

**Indraneel Mandal**

GitHub:
https://github.com/OrbIndraneel

---

⭐ If you found this project useful, feel free to **star the repository!**
