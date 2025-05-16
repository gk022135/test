from flask import Blueprint, request, jsonify
from configs.db import db, cursor

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    print("signup data is here",data);

    # Extract fields safely
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
 
    # Basic validation
    if not username or not email or not password:
        return jsonify({
            'message': 'Incomplete data received',
            'success': False,
            'status': 400
        }), 400
    print("fine 1")
    # Check if user already exists
    query_check = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query_check, (email,))
    existing_user = cursor.fetchone()
    print("fetch one \n",existing_user)

    if existing_user:
        return jsonify({
            'message': 'User already exists. Please log in.',
            'success': False,
            'status': 409
        }), 409

    # Insert new user
    query_insert = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    values = (username, email, password)
    cursor.execute(query_insert, values)
    db.commit()

    return jsonify({
        'message': 'User registered successfully',
        'success': True,
        'status': 201
    }), 201
