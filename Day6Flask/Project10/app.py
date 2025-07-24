'''
10. Student Course Enrollment 
 Features: 
 Users register/login and enroll in available courses. 
 Only logged-in users can see available courses. 
 Use current_user.id to assign enrollments. 
 Show enrollment history with flash messages. 
'''

from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db, Course
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

with app.app_context():
    db.create_all()
    # Add sample courses if not present
    if Course.query.count() == 0:
        db.session.add_all([
            Course(name='Mathematics'),
            Course(name='Physics'),
            Course(name='Chemistry')
        ])
        db.session.commit()

register_routes(app, login_manager)

if __name__ == '__main__':
    app.run(debug=True)
