from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello word i now know how to create flask apps"