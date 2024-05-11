from flask import Flask

app = Flask(__name__)


# Pagina inicio
@app.route("/")
def homepage():
    return "Bus Finder"

