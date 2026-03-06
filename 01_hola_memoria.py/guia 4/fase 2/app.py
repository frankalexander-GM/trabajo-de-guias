from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Usuario

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proyecto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

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
        return jsonify({
            "mensaje": "Usuario creado con éxito", 
            "usuario": nuevo_usuario.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "El correo ya existe o hubo un error"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)