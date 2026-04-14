from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Automatic Table Creation
with app.app_context():
    db.create_all()

# --- EXTERNAL API ROUTES ---

@app.route('/api/external-teams')
def fetch_external_teams():
    """
    Fetches football teams from an external API (football-data.org)
    """
    api_key = os.getenv('FOOTBALL_API_KEY')
    # Fetching Premier League (PL) teams
    url = "https://api.football-data.org/v4/competitions/PL/teams"
    headers = {'X-Auth-Token': api_key}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": "Failed to fetch external data", "details": str(e)}), 500

# --- INTERNAL DATABASE CRUD ROUTES ---

@app.route('/api/teams', methods=['GET', 'POST'])
def handle_teams():
    """
    GET: Returns all teams from the local database
    POST: Adds a new team to the local database
    """
    if request.method == 'POST':
        data = request.json
        if not data or 'name' not in data:
            return jsonify({"error": "Missing team name"}), 400
            
        new_team = Team(name=data['name'])
        db.session.add(new_team)
        db.session.commit()
        return jsonify({"message": "Team saved successfully"}), 201
    
    teams = Team.query.all()
    return jsonify([{"id": team.id, "name": team.name} for team in teams])

@app.route('/api/teams/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    """
    Deletes a specific team by its ID
    """
    team = Team.query.get(team_id)
    if team:
        db.session.delete(team)
        db.session.commit()
        return jsonify({"message": "Team deleted successfully"})
    
    return jsonify({"error": "Team not found"}), 404

if __name__ == '__main__':
    # Running the app on port 5000 inside the container
    app.run(host='0.0.0.0', port=5000)