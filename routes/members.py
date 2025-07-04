from flask import Blueprint, request, jsonify
from db import get_connection

member_bp = Blueprint('member_bp', __name__)

@member_bp.route('/add', methods=['POST'])
def add_member():
    data = request.get_json()
    student_id = data['student_id']
    club_id = data['club_id']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (student_id, club_id) VALUES (%s, %s)", (student_id, club_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Member added successfully'})

@member_bp.route('/remove', methods=['POST'])
def remove_member():
    data = request.get_json()
    student_id = data['student_id']
    club_id = data['club_id']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE student_id = %s AND club_id = %s", (student_id, club_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Member removed successfully'})