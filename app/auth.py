from flask import Blueprint, request, jsonify
import jwt
import datetime

auth_bp = Blueprint('auth', __name__)
SECRET_KEY = 'your_secret_key'

users = {
    'user1': 'password1',
    'user2': 'password2'
}

def generate_token(username):
    token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY, algorithm='HS256')
    return token

def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded['user']
    except jwt.ExpiredSignatureError:
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        token = generate_token(username)
        return jsonify({'token': token}), 200       
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
