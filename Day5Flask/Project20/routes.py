# routes.py

from flask import request, jsonify
from models import db, Feedback

def register_routes(app):
    @app.route('/feedback', methods=['POST'])
    def submit_feedback():
        data = request.get_json()
        try:
            fb = Feedback(
                user_name=data['user_name'],
                rating=int(data['rating']),
                comment=data['comment']
            )
            db.session.add(fb)
            db.session.commit()
            return jsonify({'message': 'Feedback submitted successfully'}), 201
        except (KeyError, ValueError) as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/feedback', methods=['GET'])
    def list_feedback():
        feedback_list = Feedback.query.all()
        return jsonify([fb.to_dict() for fb in feedback_list])

    @app.route('/feedback/<int:id>', methods=['PUT'])
    def update_feedback(id):
        fb = Feedback.query.get_or_404(id)
        data = request.get_json()

        if 'user_name' in data:
            fb.user_name = data['user_name']
        if 'rating' in data:
            try:
                fb.rating = int(data['rating'])
            except ValueError:
                return jsonify({'error': 'Rating must be an integer'}), 400
        if 'comment' in data:
            fb.comment = data['comment']

        try:
            db.session.commit()
            return jsonify({'message': 'Feedback updated successfully'})
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/feedback/<int:id>', methods=['DELETE'])
    def delete_feedback(id):
        fb = Feedback.query.get_or_404(id)
        db.session.delete(fb)
        db.session.commit()
        return jsonify({'message': 'Feedback deleted successfully'})
