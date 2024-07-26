from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    
    # Configure your app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', '3600')))

    
    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Register blueprints
    from app.routes.user_routes import api
    app.register_blueprint(api, url_prefix='/api')

    return app
