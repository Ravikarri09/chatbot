import json
import random
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

data = json.load(open(r"D:\chatbot\data\intents.json"))

model = load_model("models/dl_model.h5")
tokenizer = pickle.load(open("models/tokenizer.pkl", "rb"))
label_encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

def chatbot_response(text, history):
    text=text.lower().strip()
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=20)

    prediction = model.predict(padded)
    confidence = np.max(prediction)
    tag = label_encoder.inverse_transform([np.argmax(prediction)])[0]

    # low confidence → use context
    if confidence < 0.25:
        last_topic = None
        for h in reversed(history):
            if h["role"] == "bot" and "topic:" in h["text"]:
                last_topic = h["text"].split("topic:")[1].strip()
                break

        if last_topic:
            return f"I think you’re still asking about {last_topic}. Could you clarify?"

        return "I’m not fully sure — could you rephrase that?"

    for intent in data["intents"]:
        if intent["tag"] == tag:
            response = random.choice(intent["responses"])
            return response + f"   (topic: {tag})"
