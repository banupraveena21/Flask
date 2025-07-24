'''
15. Library Member System 
 Requirements: 
 Model: Member(id, name, email, join_date) 
 Add/view/delete members 
 List members sorted by join_date 
 Use SQLite or PostgreSQL 
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
