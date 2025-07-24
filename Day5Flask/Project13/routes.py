
from flask import request, jsonify
from datetime import datetime
from models import db, Expense

def register_routes(app):
    @app.route('/expenses', methods=['POST'])
    def add_expense():
        data = request.get_json()
        expense = Expense(
            name=data['name'],
            amount=data['amount'],
            category=data['category'],
            date=datetime.strptime(data['date'], '%Y-%m-%d').date()
        )
        db.session.add(expense)
        db.session.commit()
        return jsonify({'message': 'Expense added successfully'}), 201

    @app.route('/expenses', methods=['GET'])
    def view_expenses():
        expenses = Expense.query.all()
        return jsonify([e.to_dict() for e in expenses])

    @app.route('/expenses/<int:id>', methods=['PUT'])
    def update_expense(id):
        data = request.get_json()
        expense = Expense.query.get_or_404(id)
        expense.name = data['name']
        expense.amount = data['amount']
        expense.category = data['category']
        expense.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        db.session.commit()
        return jsonify({'message': 'Expense updated successfully'})

    @app.route('/expenses/<int:id>', methods=['DELETE'])
    def delete_expense(id):
        expense = Expense.query.get_or_404(id)
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'message': 'Expense deleted successfully'})

    @app.route('/expenses/group', methods=['GET'])
    def group_expenses():
        group_by = request.args.get('by')
        if group_by not in ['category', 'date']:
            return jsonify({'error': 'Invalid group option'}), 400

        grouped = {}
        expenses = Expense.query.all()

        for e in expenses:
            key = e.category if group_by == 'category' else e.date.isoformat()
            grouped.setdefault(key, []).append(e.to_dict())

        return jsonify(grouped)
