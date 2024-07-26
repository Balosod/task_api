from flask import jsonify
from ..models import User
from flask_jwt_extended import create_access_token, get_jwt_identity
from .. import db


def signup(data):
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "User with email already exists"}), 400
    
    new_user = User(email=data['email'],username=data['username'])
    new_user.password = data['password']
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201


def login(data):
    user = User.query.filter_by(email=data['email']).first()
    if user and user.verify_password(data['password']):
        access_token = create_access_token(identity=user.email)
        return jsonify(token=access_token,username=user.username,email=user.email), 200
    return jsonify({"message": "Username or Password incorrect"}), 401

def get_users():
    users = User.query.order_by(User.created_at.desc()).all()
    user_list = [{
      
        'username': user.username,
        'email': user.email,
       
    } for user in users]
    return jsonify(user_list), 200

def get_profile():
    email = get_jwt_identity()
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"username": user.username,"email": user.email}), 200
    return jsonify({"message": "User not found"}), 404