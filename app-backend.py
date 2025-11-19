from flask import Flask,redirect, url_for , render_template,request
import os

app = Flask(__name__)

CHAT_DIR = "chats"   # env variable for chat directory


@app.route("/<room>")
def room(room):
    return render_template("index.html")


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/api/chat/<room>", methods=["POST", "GET"])
def chat(room):
    if request.method == "POST":
        
        return 
    else:
        file_path = os.path.join(CHAT_DIR, f"{room}.txt")

        if not os.path.exists(file_path):
            return "file donest exist", 404
    
        with open(file_path, "r", encoding="utf-8") as f:
            print
            return f.read()  



if __name__ == "__main__":
    app.run()