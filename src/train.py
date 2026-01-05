import json
import numpy as np
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

data = json.load(open("D:\chatbot\data\intents.json"))

texts = []
labels = []

for intent in data["intents"]:
    for p in intent["patterns"]:
        texts.append(p)
        labels.append(intent["tag"])

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)

X = tokenizer.texts_to_sequences(texts)
X = pad_sequences(X, maxlen=20)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

model = Sequential()
model.add(Embedding(5000, 64, input_length=20))
model.add(LSTM(64, return_sequences=False))
model.add(Dropout(0.3))
model.add(Dense(32, activation="relu"))
model.add(Dense(len(set(y)), activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test))

model.save("models/dl_model.h5")

pickle.dump(tokenizer, open("models/tokenizer.pkl", "wb"))
pickle.dump(label_encoder, open("models/label_encoder.pkl", "wb"))
loss, acc = model.evaluate(X_test, y_test)
print("Validation Accuracy:", acc)


print("DL model trained & saved!")
