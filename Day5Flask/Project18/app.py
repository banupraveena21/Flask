'''
18. Subscription Manager 
 Requirements: 
 Model: Subscriber(id, email, plan, subscribed_on) 
 Add subscribers 
 Show list of active subscribers 
 Delete or update subscription plan 
 Use DateTime fields and validators
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
