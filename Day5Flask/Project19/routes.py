# routes.py

from flask import request, jsonify
from datetime import datetime
from models import db, Item

def register_routes(app):
    @app.route('/items', methods=['POST'])
    def add_item():
        data = request.get_json()
        name = data.get('name')
        quantity = data.get('quantity', 0)

        if not name or quantity < 0:
            return jsonify({'error': 'Invalid input'}), 400

        existing = Item.query.filter_by(name=name).first()
        if existing:
            return jsonify({'error': 'Item already exists'}), 400

        item = Item(name=name, quantity=quantity, updated_on=datetime.utcnow())
        db.session.add(item)
        db.session.commit()
        return jsonify({'message': 'Item added successfully'}), 201

    @app.route('/items', methods=['GET'])
    def list_items():
        items = Item.query.all()
        return jsonify([item.to_dict() for item in items])

    @app.route('/items/<int:id>', methods=['PUT'])
    def update_item(id):
        item = Item.query.get_or_404(id)
        data = request.get_json()
        qty = data.get('quantity')

        if qty is None or qty < 0:
            return jsonify({'error': 'Invalid quantity'}), 400

        item.quantity = qty
        item.updated_on = datetime.utcnow()

        # Auto-delete if quantity is 0
        if item.quantity == 0:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'message': 'Item quantity is zero. Item deleted.'})
        else:
            db.session.commit()
            return jsonify({'message': 'Item updated successfully'})

    @app.route('/items/<int:id>', methods=['DELETE'])
    def delete_item(id):
        item = Item.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully'})
