from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
scheduler = BackgroundScheduler()

# Configure Flask-Login
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"


def create_app():
    """Application Factory"""
    app = Flask(__name__)
    
    # Basic Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite for simplicity
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)
    scheduler.start()

    # Import and Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.broker_credentials import broker_bp
    from app.routes.option_chain import option_chain_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(broker_bp, url_prefix="/broker")
    app.register_blueprint(option_chain_bp, url_prefix="/option-chain")

    # Return the app instance
    return app
