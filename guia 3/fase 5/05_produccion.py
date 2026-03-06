import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/config', methods=['GET'])
def obtener_config():
    ambiente = os.getenv("FLASK_ENV", "Producción")
    puerto = os.getenv("PORT", "5000")
    return jsonify({
        "status": "Servidor seguro en línea ✅",
        "entorno": ambiente,
        "puerto": puerto
    }), 200

if __name__ == '__main__':
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    print("Fase 5 - Producción funcionando!")
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
