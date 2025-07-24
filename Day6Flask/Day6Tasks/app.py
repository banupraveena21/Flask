'''
2. Online Note-Taking App 
 Features: 
 Each user can create private notes (title, content). 
 Show a welcome message on login using current_user. 
 Only show notes that belong to the logged-in user. 
 Flash a message after creating, editing, or deleting a note. 
 Logout from navbar.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message = "Please log in to continue."

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from models import User
        db.create_all()

    from routes import main
    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
