from flask import Flask, render_template, request
from src.chatbot import chatbot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return chatbot_response(user_text,[])

if __name__ == "__main__":
    app.run(debug=True)
