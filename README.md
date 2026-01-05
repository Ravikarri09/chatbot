🎓 AI-Powered College Support Chatbot
Admissions | Exams | Placements | Scholarships | Hostel + Gamification
📌 Overview

This project is a college student support chatbot that helps students get instant answers related to:

✔ Admissions

✔ Exams & hall tickets

✔ Placements

✔ Scholarships

✔ Hostel services

The chatbot is built using:

Machine Learning (Logistic Regression)

Deep Learning (LSTM)

Flask Web Application

Gamification (Points + Badges)

It supports context-aware conversation and rewards users with badges to increase engagement.

🏗️ Project Structure
college_chatbot/
│
├── data/
│   └── intents.json
│
├── models/
│   ├── chatbot_model.pkl
│   ├── vectorizer.pkl
│   ├── dl_model.h5
│   ├── tokenizer.pkl
│   └── label_encoder.pkl
│
├── src/
│   ├── train_ml.py
│   ├── train_dl.py
│   ├── chatbot_ml.py
│   └── chatbot_dl.py
│
├── app.py
├── requirements.txt
└── templates/
    ├── index.html
    └── style.css

🔍 How It Works
1️⃣ Dataset (intents.json)

The chatbot uses an intents file containing questions (patterns) and answers (responses).

2️⃣ Model Training

Two models are trained:

Model	Use
ML (Logistic Regression)	Fast baseline classifier
DL (LSTM)	Better accuracy & context understanding
3️⃣ Context-Aware Chat

The chatbot stores conversation history and understands follow-up questions.

4️⃣ Gamification

Users earn:

⭐ Points

🏅 Badges (Beginner, Explorer, Pro)

to encourage interaction.

🚀 Installation & Setup
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Train ML Model
python src/train_ml.py

3️⃣ Train Deep Learning Model
python src/train_dl.py

4️⃣ Run the Flask App
python app.py


Then open:

http://127.0.0.1:5000

🎮 Gamification System
Feature	Description
Points	+5 per chat message
Badges	Beginner ≥20, Explorer ≥50, Pro ≥100
Motivation	Encourages student engagement

Badges appear inside chat automatically.

📊 Model Performance

After tuning and dataset expansion:

Validation Accuracy: ~70–80%


This is considered strong for FAQ-based chatbots with varied language.

✨ Features

🧠 Natural language understanding

⏳ 24×7 automated support

🎯 Context-aware conversation

🤖 ML + Deep Learning hybrid approach

🏅 Gamification (points + badges)

🌐 Simple Flask UI

🔌 Easily extendable with new topics

🔮 Future Enhancements

Voice chatbot

Multilingual support

Admin FAQ editor

BERT-based model

Leaderboard & user profiles

Database-stored chat history

🏁 Conclusion

This chatbot demonstrates how AI + Deep Learning can automate college support, reduce administrative workload, and improve student experience — while keeping the system engaging using gamification.
