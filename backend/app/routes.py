from flask import Blueprint, jsonify
import requests
import os
from .models import db, Match

main = Blueprint('main', __name__)


FOOTBALL_API_URL = "https://api.football-data.org/v4/competitions/PL/matches"
HEADERS = {"X-Auth-Token": os.getenv("c54ff48f64034dc5ba13704a91411aaf")}

@main.route('/api/futbol', methods=['GET'])
def get_futbol():
    try:
        response = requests.get(FOOTBALL_API_URL, headers=HEADERS)
        data = response.json()
        
    
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/api/db-test', methods=['GET'])
def test_db():

    return jsonify({"status": "Conectado a la DB exitosamente"}), 200