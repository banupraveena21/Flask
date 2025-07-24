from flask import request, jsonify
from models import db, Employee

def register_routes(app):
    @app.route('/employees', methods=['POST'])
    def add_employee():
        data = request.get_json()
        emp = Employee(
            name=data['name'],
            position=data['position'],
            department=data['department'],
            salary=data['salary']
        )
        db.session.add(emp)
        db.session.commit()
        return jsonify({'message': 'Employee added successfully'}), 201

    @app.route('/employees', methods=['GET'])
    def get_employees():
        department = request.args.get('department')
        query = Employee.query
        if department:
            query = query.filter_by(department=department)
        employees = query.all()
        return jsonify([e.to_dict() for e in employees])

    @app.route('/employees/<int:id>', methods=['PUT'])
    def update_employee(id):
        data = request.get_json()
        emp = Employee.query.get_or_404(id)
        emp.name = data['name']
        emp.position = data['position']
        emp.department = data['department']
        emp.salary = data['salary']
        db.session.commit()
        return jsonify({'message': 'Employee updated successfully'})

    @app.route('/employees/<int:id>', methods=['DELETE'])
    def delete_employee(id):
        emp = Employee.query.get_or_404(id)
        db.session.delete(emp)
        db.session.commit()
        return jsonify({'message': 'Employee deleted successfully'})
