from flask import Blueprint, request, jsonify, flash, get_flashed_messages
from models import db, User
from app import app, db

bp = Blueprint('routes', __name__)

def get_flash_json():
    messages = get_flashed_messages()
    return messages if messages else []

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'email', 'password')):
        return jsonify({'error': 'Missing required fields'}), 400

    if User.query.filter_by(email=data['email']).first():
        flash('Email already exists')
        return jsonify({'error': 'Email already exists', 'flash': get_flash_json()}), 400

    user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    flash('User created successfully')
    return jsonify({'message': 'User created', 'user': user.to_dict(), 'flash': get_flash_json()}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data'}), 400

    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user and existing_user.id != user.id:
            flash('Email already in use')
            return jsonify({'error': 'Email already in use', 'flash': get_flash_json()}), 400
        user.email = data['email']
    if 'password' in data:
        user.password = data['password']

    db.session.commit()
    flash('User updated successfully')
    return jsonify({'message': 'User updated', 'user': user.to_dict(), 'flash': get_flash_json()})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully')
    return jsonify({'message': 'User deleted', 'flash': get_flash_json()})
