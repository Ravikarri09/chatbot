from flask import Flask, render_template, request, session
from src.chatbot import chatbot_response

app = Flask(__name__)
app.secret_key = "your_secret_key"   # required for session

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]

    # create chat history if does not exist
    if "history" not in session:
        session["history"] = []

    # create score tracker if not exist
    if "score" not in session:
        session["score"] = 0

    # add user message
    session["history"].append({"role": "user", "text": user_text})

    # give points
    session["score"] += 5

    reply = chatbot_response(user_text, session["history"])

    # store bot reply
    session["history"].append({"role": "bot", "text": reply})

    session.modified = True

    badge_message = award_badge(session["score"])

    return reply + badge_message


def award_badge(score):
    if score >= 100:
        return "\n\n🔵 Congrats! You unlocked the **Pro User Badge**!"
    elif score >= 50:
        return "\n\n🟢 Great! You unlocked the **Explorer Badge**!"
    elif score >= 20:
        return "\n\n🟡 Nice! You unlocked the **Beginner Badge**!"
    else:
        return f"\n\n🎯 Points: {score}"


if __name__ == "__main__":
    app.run(debug=True)
