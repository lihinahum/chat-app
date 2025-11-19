from flask import Flask,redirect, url_for , render_template,request

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
        
        return 
    else:
        return 



if __name__ == "__main__":
    app.run()