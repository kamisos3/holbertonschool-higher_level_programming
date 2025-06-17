#!/bin/usr/python3
"""Adding security and authentication using API"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, generate_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)
basic_auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@app.route('/')
def home():
    return "Flask Security API is running! Use /basic-protected, /logic, etc."

@basic_auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@basic_auth.error_handler
def basic_auth_error(status):
    return jsonify({"error": "Unauthorized"}), status

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Ivalid token"}), 401

@app.route('/basic-protected')
@basic_auth.login_required
def basic_protected():
    return "Basic Auth Access Granted"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        idenity=username,
        additional_claims={"role": user['role']}
    )
    return jsonify(access_token=access_token)

@app.route('/jwt-protected')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user = users.get(current_user)

    if not user or user.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
