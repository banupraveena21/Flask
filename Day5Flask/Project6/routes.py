from flask import request, jsonify
from app import app, db
from models import Attendee

# Register attendee
@app.route('/attendees', methods=['POST'])
def register_attendee():
    data = request.get_json()
    if not all(k in data for k in ['name', 'email', 'event_name']):
        return jsonify({'error': 'Missing fields'}), 400

    if Attendee.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 409

    attendee = Attendee(name=data['name'], email=data['email'], event_name=data['event_name'])
    db.session.add(attendee)
    db.session.commit()
    return jsonify({'message': 'Attendee registered', 'attendee': attendee.to_dict()}), 201

# Get all attendees
@app.route('/attendees', methods=['GET'])
def get_attendees():
    attendees = Attendee.query.all()
    return jsonify([a.to_dict() for a in attendees]), 200

# Update attendee
@app.route('/attendees/<int:id>', methods=['PUT'])
def update_attendee(id):
    attendee = Attendee.query.get_or_404(id)
    data = request.get_json()
    attendee.name = data.get('name', attendee.name)
    attendee.email = data.get('email', attendee.email)
    attendee.event_name = data.get('event_name', attendee.event_name)
    db.session.commit()
    return jsonify({'message': 'Attendee updated', 'attendee': attendee.to_dict()}), 200

# Delete attendee
@app.route('/attendees/<int:id>', methods=['DELETE'])
def delete_attendee(id):
    attendee = Attendee.query.get_or_404(id)
    db.session.delete(attendee)
    db.session.commit()
    return jsonify({'message': 'Attendee deleted'}), 200
