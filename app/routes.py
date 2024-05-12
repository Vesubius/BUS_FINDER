from app import app
from flask import render_template


# Pagina principal
@app.route('/')
def index():
    return render_template("index.html")


@app.route("/mapa")
def Mapa():
    return "En esta Vista Debe verse el mapa"