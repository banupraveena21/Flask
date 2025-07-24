'''
6. Event Registration System 
 Requirements: 
 Model: Attendee(id, name, email, event_name) 
 Submit attendee info via form 
 Admin can: 
o View registered attendees 
o Edit or remove attendees 
 Use PostgreSQL for deployment 
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

