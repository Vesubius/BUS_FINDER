from app import app
from flask import render_template


# Pagina principal
@app.route('/')
def index():
    return render_template("index.html")


@app.route("/map")
def Mapa():
    return render_template("map.html")