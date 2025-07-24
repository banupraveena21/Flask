from flask import request, jsonify
from app import app, db
from models import Student
import validators

# Register new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    required_fields = ['name', 'roll_no', 'email', 'age']
    
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    if not validators.email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400

    if Student.query.filter_by(email=data['email']).first() or Student.query.filter_by(roll_no=data['roll_no']).first():
        return jsonify({'error': 'Email or Roll No already exists'}), 400

    student = Student(
        name=data['name'],
        roll_no=data['roll_no'],
        email=data['email'],
        age=data['age']
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Student registered successfully', 'student': student.to_dict()}), 201

# View all students
@app.route('/students', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students]), 200

# View a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict()), 200

# Update student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()

    if 'email' in data and not validators.email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400

    student.name = data.get('name', student.name)
    student.roll_no = data.get('roll_no', student.roll_no)
    student.email = data.get('email', student.email)
    student.age = data.get('age', student.age)
    db.session.commit()
    return jsonify({'message': 'Student updated successfully', 'student': student.to_dict()}), 200

# Delete student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'}), 200
