'''
12. Appointment Booking App 
 Requirements: 
 Model: Appointment(id, name, date, time, status) 
 Users can book appointments via form 
 Admin can view and update status (confirmed/canceled) 
 Delete expired appointments
'''

from flask import Flask
from config import Config
from models import db
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
