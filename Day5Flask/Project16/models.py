
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Complaint(db.Model):
    __tablename__ = 'complaints'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    resolved = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'message': self.message,
            'resolved': self.resolved
        }
