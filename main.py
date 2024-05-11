from flask import Flask

app = Flask(__name__)


#inicio
@app.route("/")
def Seleccion_de_Ruta():
    return "Bus Finder"


#Mapa
@app.route("/Mapa")
def Mapa():
    return "GoogleMaps.PNG"