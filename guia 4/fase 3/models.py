from flask_sqlalchemy import SQLAlchemy

# Inicializamos la extensión
db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    # Columnas de la base de datos
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # Método para convertir a diccionario (excluye la contraseña por seguridad)
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
        }