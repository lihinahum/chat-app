from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

CHAT_DIR = "chats"   # env variable for chat directory

#Implementated by #Lihi
@app.route("/<room>")
def room(room):
    return render_template("index.html")

#Implementated by #Salih
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


#Implementated by #Lihi
@app.route("/api/chat/<room>", methods=["POST", "GET"])
def chat(room):
    if request.method == "POST":
        username = request.form.get("username")
        message = request.form.get("msg")
        if not message :
            return "message is required", 200
        if not username:
            return "username is required", 200
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(f"chats/{room}.txt", "a") as f:
            f.write(f"[{timestamp}] {username}: {message}\n")

        return "Message sent", 200
    
    #Implementated by #Salih       
    else:
        file_path = os.path.join(CHAT_DIR, f"{room}.txt")
        if not os.path.exists(file_path):
            return "" , 200
    
        with open(file_path, "r", encoding="utf-8") as f:
            
            return f.read()
   


if __name__ == "__main__":
    app.run()