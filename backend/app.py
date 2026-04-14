from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)
CORS(app)

# DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

# --- RUTAS API EXTERNA ---
@app.route('/api/external-teams')
def get_external_teams():
    api_key = os.getenv('FOOTBALL_API_KEY')
    # Traemos los equipos de la Premier League (PL)
    url = "https://api.football-data.org/v4/competitions/PL/teams"
    headers = {'X-Auth-Token': api_key}
    try:
        response = requests.get(url, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- RUTAS CRUD INTERNO (TU BD) ---
@app.route('/api/teams', methods=['GET', 'POST'])
def manage_teams():
    if request.method == 'POST':
        data = request.json
        new_team = Team(name=data['name'])
        db.session.add(new_team)
        db.session.commit()
        return jsonify({"message": "Equipo guardado"}), 201
    
    teams = Team.query.all()
    return jsonify([{"id": t.id, "name": t.name} for t in teams])

@app.route('/api/teams/<int:id>', methods=['DELETE'])
def delete_team(id):
    team = Team.query.get(id)
    if team:
        db.session.delete(team)
        db.session.commit()
        return jsonify({"message": "Eliminado"})
    return jsonify({"error": "No encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)