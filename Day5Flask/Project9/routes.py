
from flask import request, jsonify
from models import db, Application

def register_routes(app):
    @app.route('/applications', methods=['POST'])
    def add_application():
        data = request.get_json()
        new_app = Application(
            name=data['name'],
            email=data['email'],
            job_title=data['job_title'],
            status=data.get('status', 'applied')
        )
        db.session.add(new_app)
        db.session.commit()
        return jsonify({'message': 'Application added successfully'}), 201

    @app.route('/applications/<int:id>', methods=['PUT'])
    def update_status(id):
        data = request.get_json()
        app_entry = Application.query.get_or_404(id)
        app_entry.status = data['status']
        db.session.commit()
        return jsonify({'message': 'Status updated successfully'})

    @app.route('/applications', methods=['GET'])
    def get_applications():
        status = request.args.get('status')
        query = Application.query
        if status:
            query = query.filter_by(status=status)
        apps = query.all()
        return jsonify([app.to_dict() for app in apps])
