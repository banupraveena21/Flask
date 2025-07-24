
from flask import request, jsonify
from datetime import datetime
import re
from models import db, Subscriber

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def register_routes(app):
    @app.route('/subscribers', methods=['POST'])
    def add_subscriber():
        data = request.get_json()
        email = data.get('email')
        plan = data.get('plan')
        subscribed_on_str = data.get('subscribed_on')

        if not email or not re.match(EMAIL_REGEX, email):
            return jsonify({'error': 'Invalid email format'}), 400
        if not plan:
            return jsonify({'error': 'Plan is required'}), 400

        try:
            subscribed_on = datetime.fromisoformat(subscribed_on_str) if subscribed_on_str else datetime.utcnow()
        except ValueError:
            return jsonify({'error': 'Invalid datetime format for subscribed_on. Use ISO format.'}), 400

        existing = Subscriber.query.filter_by(email=email).first()
        if existing:
            return jsonify({'error': 'Email already subscribed'}), 400

        subscriber = Subscriber(email=email, plan=plan, subscribed_on=subscribed_on)
        db.session.add(subscriber)
        db.session.commit()
        return jsonify({'message': 'Subscriber added successfully'}), 201

    @app.route('/subscribers', methods=['GET'])
    def list_subscribers():
        subscribers = Subscriber.query.all()
        return jsonify([s.to_dict() for s in subscribers])

    @app.route('/subscribers/<int:id>', methods=['PUT'])
    def update_subscriber(id):
        subscriber = Subscriber.query.get_or_404(id)
        data = request.get_json()

        plan = data.get('plan')
        if plan:
            subscriber.plan = plan
        
        subscribed_on_str = data.get('subscribed_on')
        if subscribed_on_str:
            try:
                subscriber.subscribed_on = datetime.fromisoformat(subscribed_on_str)
            except ValueError:
                return jsonify({'error': 'Invalid datetime format for subscribed_on. Use ISO format.'}), 400

        db.session.commit()
        return jsonify({'message': 'Subscriber updated successfully'})

    @app.route('/subscribers/<int:id>', methods=['DELETE'])
    def delete_subscriber(id):
        subscriber = Subscriber.query.get_or_404(id)
        db.session.delete(subscriber)
        db.session.commit()
        return jsonify({'message': 'Subscriber deleted successfully'})
