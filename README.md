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

## 👨‍💻 Author

**Indraneel Mandal**

GitHub:
https://github.com/OrbIndraneel

---

⭐ If you found this project useful, feel free to **star the repository!**
