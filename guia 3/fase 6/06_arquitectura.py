import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

class InventarioTrapiche:
    def __init__(self):
        self.productos = []

    def agregar_lote(self, tipo: str, kilos: float) -> dict:
        lote = {
            "id": len(self.productos) + 1,
            "tipo": tipo,
            "kilos": kilos
        }
        self.productos.append(lote)
        return lote

    def obtener_todos(self) -> list:
        return self.productos

gestor = InventarioTrapiche()

@app.route('/api/inventario', methods=['GET'])
def ver_inventario():
    datos = gestor.obtener_todos()
    return jsonify({"total": len(datos), "lotes": datos}), 200

@app.route('/api/inventario', methods=['POST'])
def registrar_lote():
    try:
        payload = request.get_json()
        nuevo = gestor.agregar_lote(payload["tipo"], payload["kilos"])
        return jsonify({"mensaje": "Lote registrado", "data": nuevo}), 201
    except KeyError:
        return jsonify({"error": "Datos incompletos"}), 400

if __name__ == '__main__':
    print("Fase 6 - Arquitectura de Capas funcionando!")
    app.run(host='0.0.0.0', port=5000, debug=True)
