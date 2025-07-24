from flask import request, jsonify
from app import app, db
from models import Task
from datetime import datetime

# Add new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    due_date = data.get('due_date')

    if not title:
        return jsonify({'error': 'Title is required'}), 400

    try:
        due_date_obj = datetime.fromisoformat(due_date) if due_date else None
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400

    task = Task(title=title, due_date=due_date_obj)
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created', 'task': task.to_dict()}), 201

# View all tasks ordered by due date
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.order_by(Task.due_date).all()
    return jsonify([t.to_dict() for t in tasks]), 200

# Mark task as done or undone
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.is_done = data.get('is_done', task.is_done)
    db.session.commit()
    return jsonify({'message': 'Task updated', 'task': task.to_dict()}), 200

# Delete completed tasks
@app.route('/tasks/completed', methods=['DELETE'])
def delete_completed_tasks():
    deleted = Task.query.filter_by(is_done=True).delete()
    db.session.commit()
    return jsonify({'message': f'{deleted} completed task(s) deleted'}), 200
