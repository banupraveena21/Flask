'''
4. Student Database System 
 Requirements: 
 Model: Student(id, name, roll_no, email, age) 
 Allow new student registration 
 View, update, and delete student profiles 
 Use validators.Email for validation 
 Use MySQL or SQLite
'''

from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from routes import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
