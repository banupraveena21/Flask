'''
8. Contact Directory 
 Requirements: 
 Model: Contact(id, name, phone, email, address) 
 Add, edit, delete contacts 
 Use email and phone validators 
 Use SQLite and Flask-WTF forms 
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
