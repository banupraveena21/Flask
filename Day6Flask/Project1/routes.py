# routes.py

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from models import db, User, Task

def register_routes(app, login_manager):
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    @login_required
    def home():
        return render_template('home.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if len(password) < 8:
                flash('Password must be at least 8 characters.', 'error')
                return redirect(url_for('register'))

            if User.query.filter_by(username=username).first():
                flash('Username already exists.', 'error')
                return redirect(url_for('register'))

            user = User(username=username)
            try:
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                flash('Registration successful. Please log in.', 'success')
                return redirect(url_for('login'))
            except ValueError as e:
                flash(str(e), 'error')
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Logged in successfully.', 'success')
                return redirect(url_for('tasks'))
            else:
                flash('Invalid credentials.', 'error')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Logged out successfully.', 'success')
        return redirect(url_for('login'))

    @app.route('/tasks')
    @login_required
    def tasks():
        user_tasks = Task.query.filter_by(user_id=current_user.id).all()
        return render_template('tasks.html', tasks=user_tasks)

    @app.route('/tasks/add', methods=['POST'])
    @login_required
    def add_task():
        title = request.form['title']
        due_date = request.form['due_date']
        if not title or not due_date:
            flash('All fields are required.', 'error')
        else:
            task = Task(title=title, due_date=due_date, user_id=current_user.id)
            db.session.add(task)
            db.session.commit()
            flash('Task added.', 'success')
        return redirect(url_for('tasks'))

    @app.route('/tasks/<int:id>/toggle')
    @login_required
    def toggle_task(id):
        task = Task.query.get_or_404(id)
        if task.user_id != current_user.id:
            flash('Unauthorized action.', 'error')
            return redirect(url_for('tasks'))
        task.completed = not task.completed
        db.session.commit()
        flash('Task status updated.', 'success')
        return redirect(url_for('tasks'))

    @app.route('/tasks/<int:id>/delete')
    @login_required
    def delete_task(id):
        task = Task.query.get_or_404(id)
        if task.user_id != current_user.id:
            flash('Unauthorized action.', 'error')
            return redirect(url_for('tasks'))
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted.', 'success')
        return redirect(url_for('tasks'))
