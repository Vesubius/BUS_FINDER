from flask import Flask

app = Flask(__name__)

@app.route("/home")
def Home():
    return "Bus Finder"