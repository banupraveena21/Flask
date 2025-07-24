
from flask import request, jsonify
from datetime import datetime
from models import db, Member

def register_routes(app):
    @app.route('/members', methods=['POST'])
    def add_member():
        data = request.get_json()
        member = Member(
            name=data['name'],
            email=data['email'],
            join_date=datetime.strptime(data['join_date'], '%Y-%m-%d').date()
        )
        db.session.add(member)
        db.session.commit()
        return jsonify({'message': 'Member added successfully'}), 201

    @app.route('/members', methods=['GET'])
    def get_members():
        members = Member.query.order_by(Member.join_date).all()
        return jsonify([m.to_dict() for m in members])

    @app.route('/members/<int:id>', methods=['DELETE'])
    def delete_member(id):
        member = Member.query.get_or_404(id)
        db.session.delete(member)
        db.session.commit()
        return jsonify({'message': 'Member deleted successfully'})
