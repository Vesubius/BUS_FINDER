from app import app


# Pagina principal 
@app.route('/')
def index():
    return "¡Hola, mundo!"


@app.route("/Mapa")
def Mapa():
    return "En esta Vista Debe verse el mapa"