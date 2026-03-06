from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Usuario

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proyecto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# --- RUTA DE REGISTRO (Ya la tenías) ---
@app.route('/api/usuarios', methods=['POST'])
def registrar_usuario():
    datos = request.get_json()
    nuevo_usuario = Usuario(
        nombre=datos['nombre'],
        email=datos['email'],
        password=datos['password']
    )
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify({"mensaje": "Usuario creado", "usuario": nuevo_usuario.to_dict()}), 201
    except:
        return jsonify({"error": "Error al registrar"}), 400

# --- NUEVA RUTA: LOGIN DE USUARIOS ---
@app.route('/api/login', methods=['POST'])
def login():
    datos = request.get_json()
    # 1. Buscamos al usuario por su correo
    usuario = Usuario.query.filter_by(email=datos['email']).first()

    # 2. Verificamos si existe y si la contraseña coincide
    if usuario and usuario.password == datos['password']:
        return jsonify({
            "mensaje": "¡Login exitoso!",
            "usuario": usuario.to_dict()
        }), 200
    else:
        return jsonify({"error": "Correo o contraseña incorrectos"}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)