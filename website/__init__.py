from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # Creating Flask application
    app = Flask(__name__)

    # Web server will be encrypted using this key
    app.config['SECRET_KEY'] = "Pizza is awesome"

    # Telling Flask where the database is lcoated
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Tell database which app is being used
    db.init_app(app)

    # Letting Flask know of the other routes
    from .views import views
    from .auth import auth

    # Registering Blueprints; url_prefix applies to the URL specified in the Python files
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Creating the databases
    from .models import User, Note
    create_database(app)

    # Create login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # User this function to load user
    @login_manager.user_loader
    def load_user(id):
        # Identify user using the ID (primary key)
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created database!")