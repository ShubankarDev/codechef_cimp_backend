from flask import Blueprint, request, jsonify
from db import get_connection

role_bp = Blueprint('role_bp', __name__)

@role_bp.route('/assign-president', methods=['POST'])
def assign_president():
    data = request.get_json()
    student_id = data.get('student_id')
    club_id = data.get('club_id')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE clubs SET president_id = %s WHERE id = %s", (student_id, club_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'President assigned successfully'})

@role_bp.route('/assign-faculty', methods=['POST'])
def assign_faculty():
    data = request.get_json()
    faculty_id = data.get('faculty_id')
    club_id = data.get('club_id')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE clubs SET faculty_id = %s WHERE id = %s", (faculty_id, club_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Faculty coordinator assigned successfully'})
