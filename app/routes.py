from flask import Blueprint, request, send_file, jsonify
import os
from .auth import verify_token

main_bp = Blueprint('main', __name__)

@main_bp.route('/files/<path:filename>')
def serve_file(filename):
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing'}), 401

    username = verify_token(token)
    if not username:
        return jsonify({'message': 'Invalid token'}), 401

    file_path = os.path.join('C:\\xampp\\htdocs\\tes', filename)
    
    # console file_path
    print(file_path)

    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return jsonify({'message': 'File not found'}), 404
