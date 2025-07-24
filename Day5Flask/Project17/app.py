'''
17. Blog Commenting System 
 Requirements: 
 Models: Post(id, title, content), Comment(id, post_id, content) 
 Submit comments under each post 
 View comments inline 
 Use foreign key for post-comment relationship
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
