from flask import Blueprint, request, jsonify
from db import get_connection

club_bp = Blueprint('club_bp', __name__)

@club_bp.route('/create', methods=['POST'])
def create_club():
    data = request.get_json()
    name = data['name']
    desc = data['description']
    category = data['category']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clubs (name, description, category) VALUES (%s, %s, %s)", (name, desc, category))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Club created successfully'})

@club_bp.route('/all', methods=['GET'])
def get_all_clubs():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clubs")
    clubs = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(clubs)