'''
9. Job Application Tracker 
 Requirements: 
 Model: Application(id, name, email, job_title, status) 
 Add applications via form 
 Update status (applied, shortlisted, rejected) 
 View all applications with filter by status 
 Use PostgreSQL for production-ready structure 
'''

# app.py

from flask import Flask
from config import Config
from models import db
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from routes import *
with app.app_context():
    db.create_all()

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
