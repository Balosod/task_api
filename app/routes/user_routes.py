from flask import Blueprint, request,jsonify
from flask_jwt_extended import jwt_required
from app.services.user_service import signup, login,get_users,get_profile
from app.validation_schema.user_validation_schema import SignupValidationSchema,LoginValidationSchema
from marshmallow import  ValidationError


api = Blueprint('api', __name__)

@api.route('/signup', methods=['POST'])
def signup_route():
    schema = SignupValidationSchema()
    try:
        data = schema.load(request.json)
        return signup(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    

@api.route('/login', methods=['POST'])
def login_route():
    schema = LoginValidationSchema()
    try:
        data = schema.load(request.json)
        return login(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
   

@api.route('/users', methods=['GET'])
@jwt_required()
def get_users_route():
   return get_users()

@api.route('/profile', methods=['GET'])
@jwt_required()
def get_profile_route():
   return get_profile()
