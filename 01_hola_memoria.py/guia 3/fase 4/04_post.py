from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios_db = []

@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    # Recibe JSON del cliente
    datos = request.get_json()
    
    if not datos or "nombre" not in datos:
        return jsonify({"error": "Falta 'nombre'"}), 400
    
    nuevo_usuario = {
        "id": len(usuarios_db) + 1,
        "nombre": datos["nombre"],
        "rol": datos.get("rol", "Usuario")
    }
    
    usuarios_db.append(nuevo_usuario)
    return jsonify({"mensaje": "Creado!", "data": nuevo_usuario}), 201

@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({"usuarios": usuarios_db})

if __name__ == '__main__':
    print("Fase 4 - POST funcionando!")
    app.run(host='0.0.0.0', port=5000, debug=True)
