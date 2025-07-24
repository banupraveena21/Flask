
from flask import request, jsonify
from models import db, Complaint

def register_routes(app):
    @app.route('/complaints', methods=['POST'])
    def submit_complaint():
        data = request.get_json()
        complaint = Complaint(
            name=data['name'],
            message=data['message'],
            resolved=False
        )
        db.session.add(complaint)
        db.session.commit()
        return jsonify({'message': 'Complaint submitted successfully'}), 201

    @app.route('/complaints', methods=['GET'])
    def list_complaints():
        complaints = Complaint.query.all()
        return jsonify([c.to_dict() for c in complaints])

    @app.route('/complaints/<int:id>', methods=['PUT'])
    def mark_resolved(id):
        complaint = Complaint.query.get_or_404(id)
        data = request.get_json()
        complaint.resolved = data.get('resolved', complaint.resolved)
        db.session.commit()
        return jsonify({'message': 'Complaint status updated'})

    @app.route('/complaints/<int:id>', methods=['DELETE'])
    def delete_complaint(id):
        complaint = Complaint.query.get_or_404(id)
        db.session.delete(complaint)
        db.session.commit()
        return jsonify({'message': 'Complaint deleted successfully'})

    @app.route('/complaints/stats', methods=['GET'])
    def complaint_stats():
        total = Complaint.query.count()
        resolved = Complaint.query.filter_by(resolved=True).count()
        return jsonify({'total_complaints': total, 'resolved_complaints': resolved})
