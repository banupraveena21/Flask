from flask import request, jsonify
from app import app, db
from models import Contact
import re
from email_validator import validate_email, EmailNotValidError

# Phone number validator
def is_valid_phone(phone):
    return re.match(r'^[6-9]\d{9}$', phone)

# Add contact
@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    if not all(k in data for k in ['name', 'phone', 'email']):
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate email and phone
    try:
        validate_email(data['email'])
    except EmailNotValidError:
        return jsonify({'error': 'Invalid email'}), 400

    if not is_valid_phone(data['phone']):
        return jsonify({'error': 'Invalid phone number'}), 400

    contact = Contact(**data)
    db.session.add(contact)
    db.session.commit()
    return jsonify({'message': 'Contact added', 'contact': contact.to_dict()}), 201

# Get all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([c.to_dict() for c in contacts]), 200

# Update contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    contact = Contact.query.get_or_404(id)
    data = request.get_json()

    if 'email' in data:
        try:
            validate_email(data['email'])
        except EmailNotValidError:
            return jsonify({'error': 'Invalid email'}), 400
        contact.email = data['email']

    if 'phone' in data:
        if not is_valid_phone(data['phone']):
            return jsonify({'error': 'Invalid phone number'}), 400
        contact.phone = data['phone']

    contact.name = data.get('name', contact.name)
    contact.address = data.get('address', contact.address)

    db.session.commit()
    return jsonify({'message': 'Contact updated', 'contact': contact.to_dict()}), 200

# Delete contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contact deleted'}), 200
