from flask import Flask, jsonify
from models import db, Usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proyecto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return jsonify({"mensaje": "Base de datos conectada con éxito"})

if __name__ == '__main__':
    app.run(debug=True)