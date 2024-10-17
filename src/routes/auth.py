from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from src.models import User, Role
from src.db import db

from datetime import timedelta
from hashlib import sha256

auth_bp = Blueprint("auth", __name__)
jwt = JWTManager

@auth_bp.post('/sign-up')
def create_user():
    data = request.get_json()

    username = data.get('username', None)
    email = data.get('email', None)
    password = data.get('password', None)
    social_networks = data.get('social_networks', None)

    if username is None or email is None or password is None:
        return jsonify ({"msg": "username, email and password are required"}), 400
    
    new_user = User.query.filter_by(username=username).first()
    if new_user is not None:
        return jsonify({"msg": "username already taken"}), 400
    
    role_user = Role.query.filter_by(role_name="USER").first()
    user = User(username, email, sha256(password.encode()).hexdigest(), social_networks, role_user.role_id)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "msg": "Was created a new user",
        "data": {
            "username": username,
            "email": email,
            "role": role_user.role_name
        }
    }), 201

@auth_bp.post("/sign-in")
def login():
    data = request.get_json()

    username = data.get('username', None)
    password = data.get('password', None)

    if username is None or password is None:
        return jsonify({"msg": "username and password are required"})
    
    user = User.query.filter_by(username=username).first_or_404("username is not found")

    if user.username == username and user.password == sha256(password.encode()).hexdigest():
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=3))
        return jsonify(access_token=access_token)
    else:
        return({"msg": "username or password incorrect"})
    

@auth_bp.get("/get-me")
@jwt_required()
def get_me():
    user_id = get_jwt_identity()
    user = User.query.filter_by(username=user_id).first_or_404("identity is not found")
    return jsonify(user.to_dict())
