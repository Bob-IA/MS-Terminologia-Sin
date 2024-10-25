from flask import Flask, request, jsonify

app = Flask(__name__)

SINONIMOS = {
    "lija": ["papel de lija", "abrasivo", "esmeril"],
    "destornillador": ["desatornillador", "desarmador", "atornillador"],
    "martillo": ["mazo", "marrón", "maceta", "martillo de carpintero", "martillo de bola"],
    "alicate": ["pinza", "tenaza", "pince", "pico de loro"],
    "taladro": ["perforadora", "drill", "bareno"],
    "galleta":["esmeril angular", "amoladora", "pulidora", "radial", "rebarbadora", "discos del esmeril"],
    "amoladora": ["esmeril angular", "pulidora", "radial", "galleta", "rebarbadora"],
    "llave inglesa": ["llave ajustable", "francesa", "llave crescent", "llave española"],
    "cinta métrica": ["metro", "wincha", "flexómetro", "cinta de medir"],
    "caladora": ["sierra caladora", "sierra de vaivén", "sierra de calado", "sierra de marquetería"],
    "cincel": ["escoplo", "formón", "escoplo de albañil"],
    "carretilla": ["volqueta", "carrucha", "vagoneta", "carretón"],
    "palanca": ["barra de uña", "pie de cabra", "pata de cabra", "barreta"],
    "serrucho": ["sierra manual", "sierrucho", "serrote"],
    "espatula": ["llana", "plana", "espátula", "espátula para yeso", "plana de albañil"],
    "pala": ["lampa", "pico", "excavadora", "pala de punta", "pala plana"],
    "nivel de burbuja": ["nivel", "nivelador", "nivel de albañil", "nivel de mano"],
    "manguera de nivel": ["manguera", "manguera de agua", "tubo de nivelación"],
    "escuadra": ["ángulo", "escuadra metálica", "escuadra de carpintero"],
    "lápiz de carpintero": ["marcador de carpintero", "lápiz de obra", "lápiz para madera"],
    "destornillador de cruz": ["cruceta", "estrella", "phillips"],
    "llave de tubo": ["llave caño", "llave pipa", "llave de carraca", "llave para cañerías"],
    "limpia vidrios": ["jalador", "secador de vidrios", "espátula para vidrios", "limpiacristales"],
    "escalera": ["andamio", "escalerilla", "escalera de mano", "escalera plegable"],
    "soplete": ["mechero", "quemador", "lanzallamas de soldadura"],
    "brocha": ["pincel", "brochón", "pincel grande", "brocha gorda"],
    "rodillo": ["palo de pintura", "pintador", "rodillo de pintura", "rodillo para paredes"],
    "llave stillson": ["llave grifa", "llave de tubo", "llave para caños", "llave sueca"],
    "esmeriladora": ["galleta", "pulidora", "rebarbadora", "desbastadora"],
    "cincel para concreto": ["puntero", "barreta", "cincel de albañil", "escarpa"],
    "pico": ["pico pala", "pico de obra", "pico de albañil"],
    "machete": ["cortador", "corta-maleza", "podón", "cuchilla"],
    "llave de impacto": ["llave neumática", "pistola de impacto", "atornilladora de impacto"],
    "sierra circular": ["circular", "disco de corte", "tronzadora"],
    "corta hierro": ["cizalla", "cortadora de varilla", "corta barras", "tenaza cortadora"],
    "espatula ancha": ["llana ancha", "plana gruesa", "llana de acabado"],
    "compresor de aire": ["compresor", "máquina de aire", "soplador de aire"],
    "pico de albañil": ["cincel", "martillo de albañil", "pico martillo"],
    "cincel de madera": ["formón de madera", "gubia", "cincel de carpintero"],
}

@app.route('/sinonimos', methods=['POST'])
def obtener_sinonimos():
    data = request.json
    producto = data.get("producto", "").lower()
    sinonimos = SINONIMOS.get(producto, [producto])  # Devuelve el término original si no encuentra sinónimos
    return jsonify({"sinonimos": sinonimos})

if __name__ == '__main__':
    app.run(port=8081)  # Puerto para el microservicio de sinónimos