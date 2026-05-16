from flask import Flask, render_template, request, jsonify
from modules.chatbot import chatbot_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data["message"]

    bot_response = chatbot_response(user_message)

    return jsonify({
        "response": bot_response
    })


if __name__ == "__main__":
    app.run(debug=True)