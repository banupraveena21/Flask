'''
10. Simple Voting System 
 Requirements: 
 Models: Candidate(id, name, party) and Vote(id, voter_name, candidate_id) 
 Voters cast votes via form 
 Admin can see vote count per candidate 
 Prevent duplicate voting via name check 
 Use foreign key relationships
'''

# app.py

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
