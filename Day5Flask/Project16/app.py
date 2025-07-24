'''
16. Complaint Submission Portal 
 Requirements: 
 Model: Complaint(id, name, message, resolved) 
 Users submit complaints 
 Admin can mark as resolved or delete 
 Show total complaints vs resolved count
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
