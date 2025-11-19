from flask import Flask, render_template, request
import os
from datetime import datetime
import mysql.connector

app = Flask(__name__)


def get_db():
    return mysql.connector.connect(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),
                                   password=os.getenv("DB_PASS"),database=os.getenv("DB_NAME"))

# Implemented by #Lihi
@app.route("/<room>")
def room(room):
    return render_template("index.html")

# Implemented by #Salih
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

# Implemented by #Lihi & #Salih
@app.route("/api/chat/<room>", methods=["POST", "GET"])
def chat(room):
    if request.method == "POST":
        username = request.form.get("username")
        message = request.form.get("msg")

        if not message:
            return "message is required", 400
        if not username:
            return "username is required", 400
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO messages (room_number, username, message, timestamp) VALUES (%s, %s, %s, %s)",
            (room, username, message, timestamp)
        )
        db.commit()
        cursor.close()
        db.close()
        return "Message sent", 200
    else:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "SELECT timestamp, username, message FROM messages WHERE room_number=%s ORDER BY id ASC",
            (room,)
        )
        rows = cursor.fetchall()
        cursor.close()
        db.close()
        output = ""
        for timestamp, username, message in rows:
            output += f"[{timestamp}] {username}: {message}\n"
        return output, 200
    


if __name__ == "__main__":
    app.run(host="0.0.0.0")