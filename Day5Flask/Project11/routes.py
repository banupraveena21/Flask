
from flask import request, jsonify
from models import db, Student, Course, Enrollment

def register_routes(app):
    @app.route('/students', methods=['POST'])
    def add_student():
        data = request.get_json()
        student = Student(name=data['name'])
        db.session.add(student)
        db.session.commit()
        return jsonify({'message': 'Student added'}), 201

    @app.route('/courses', methods=['POST'])
    def add_course():
        data = request.get_json()
        course = Course(name=data['name'], fee=data['fee'])
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'Course added'}), 201

    @app.route('/enrollments', methods=['POST'])
    def enroll_student():
        data = request.get_json()
        enrollment = Enrollment(student_id=data['student_id'], course_id=data['course_id'])
        db.session.add(enrollment)
        db.session.commit()
        return jsonify({'message': 'Student enrolled'}), 201

    @app.route('/enrollments', methods=['GET'])
    def view_enrollments():
        enrollments = Enrollment.query.all()
        return jsonify([e.to_dict() for e in enrollments])

    @app.route('/enrollments/<int:id>', methods=['PUT'])
    def update_enrollment(id):
        data = request.get_json()
        enrollment = Enrollment.query.get_or_404(id)
        enrollment.student_id = data['student_id']
        enrollment.course_id = data['course_id']
        db.session.commit()
        return jsonify({'message': 'Enrollment updated'})

    @app.route('/enrollments/<int:id>', methods=['DELETE'])
    def delete_enrollment(id):
        enrollment = Enrollment.query.get_or_404(id)
        db.session.delete(enrollment)
        db.session.commit()
        return jsonify({'message': 'Enrollment deleted'})
