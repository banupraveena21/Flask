'''
18. Event RSVP System (Per User) 
 Features: 
 Login required to RSVP for events. 
 Use Flash to confirm RSVP. 
 View and update RSVPs from dashboard. 
 Use session to store recently RSVP’d event.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
