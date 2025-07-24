
from flask import request, jsonify
from datetime import datetime, date
from models import db, Appointment

def register_routes(app):
    @app.route('/appointments', methods=['POST'])
    def book_appointment():
        data = request.get_json()
        appointment = Appointment(
            name=data['name'],
            date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
            time=datetime.strptime(data['time'], '%H:%M').time(),
            status=data.get('status', 'pending')
        )
        db.session.add(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment booked successfully'}), 201

    @app.route('/appointments', methods=['GET'])
    def view_appointments():
        appointments = Appointment.query.all()
        return jsonify([a.to_dict() for a in appointments])

    @app.route('/appointments/<int:id>', methods=['PUT'])
    def update_status(id):
        data = request.get_json()
        appointment = Appointment.query.get_or_404(id)
        appointment.status = data['status']
        db.session.commit()
        return jsonify({'message': 'Appointment status updated'})

    @app.route('/appointments/expired', methods=['DELETE'])
    def delete_expired():
        today = date.today()
        expired = Appointment.query.filter(Appointment.date < today).all()
        for appt in expired:
            db.session.delete(appt)
        db.session.commit()
        return jsonify({'message': f'{len(expired)} expired appointments deleted'})
