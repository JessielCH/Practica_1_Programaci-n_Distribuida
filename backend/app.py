from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)
CORS(app)

# Configuración de la DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la tabla
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Crear tablas automáticamente
with app.app_context():
    db.create_all()

# --- RUTAS ---

@app.route('/')
def home():
    return jsonify({"status": "Backend, DB y API conectados", "user": "Jessiel JD"})

@app.route('/api/partidos')
def get_matches():
    api_key = os.getenv('FOOTBALL_API_KEY')
    url = "https://api.football-data.org/v4/competitions/PL/matches"
    headers = {'X-Auth-Token': api_key}
    try:
        response = requests.get(url, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/test-db-write')
def test_db_write():
    try:
        # Insertamos un equipo de prueba
        nuevo = Team(name="LDU Quito")
        db.session.add(nuevo)
        db.session.commit()
        
        # Consultamos para verificar
        todos = Team.query.all()
        return jsonify([{"id": t.id, "name": t.name} for t in todos])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)