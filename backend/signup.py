from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
import uuid

app = Flask(__name__)

# In-memory user store (use a real database in production)
users = {}

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # Validate required fields
    if not data or not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'error': 'Missing fields'}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    # Check if user already exists (by email)
    if email in users:
        return jsonify({'error': 'User already exists'}), 409

    # Hash password
    hashed_password = generate_password_hash(password)

    # Create a new user entry
    user_id = str(uuid.uuid4())
    users[email] = {
        'id': user_id,
        'username': username,
        'email': email,
        'password': hashed_password
    }

    return jsonify({'message': 'Signup successful', 'user_id': user_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
