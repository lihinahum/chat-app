from flask import Flask,redirect, url_for , render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/<room>")
def room(room):
    return render_template("index.html")


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/api/chat/<room>", methods=["POST", "GET"])
def chat(room):
    if request.method == "POST":
        username = request.form.get("username")
        message = request.form.get("msg")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(f"chats/{room}.txt", "a") as f:
            f.write(f"[{timestamp}] {username}: {message}\n")

        return "Message sent", 200
   


if __name__ == "__main__":
    app.run()