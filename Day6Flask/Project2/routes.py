# routes.py

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from models import db, User, Note

def register_routes(app, login_manager):
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if User.query.filter_by(username=username).first():
                flash("Username already exists", 'error')
                return redirect(url_for('register'))
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash("Registration successful. Please log in.", 'success')
            return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user and user.check_password(request.form['password']):
                login_user(user)
                flash(f"Welcome, {user.username}!", 'success')
                return redirect(url_for('notes'))
            flash("Invalid credentials", 'error')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("You have been logged out.", 'success')
        return redirect(url_for('login'))

    @app.route('/notes')
    @login_required
    def notes():
        user_notes = Note.query.filter_by(user_id=current_user.id).all()
        return render_template('notes.html', notes=user_notes)

    @app.route('/notes/add', methods=['POST'])
    @login_required
    def add_note():
        title = request.form['title']
        content = request.form['content']
        note = Note(title=title, content=content, user_id=current_user.id)
        db.session.add(note)
        db.session.commit()
        flash("Note added successfully", 'success')
        return redirect(url_for('notes'))

    @app.route('/notes/<int:id>/edit', methods=['POST'])
    @login_required
    def edit_note(id):
        note = Note.query.get_or_404(id)
        if note.user_id != current_user.id:
            flash("Unauthorized", 'error')
            return redirect(url_for('notes'))
        note.title = request.form['title']
        note.content = request.form['content']
        db.session.commit()
        flash("Note updated successfully", 'success')
        return redirect(url_for('notes'))

    @app.route('/notes/<int:id>/delete')
    @login_required
    def delete_note(id):
        note = Note.query.get_or_404(id)
        if note.user_id != current_user.id:
            flash("Unauthorized", 'error')
            return redirect(url_for('notes'))
        db.session.delete(note)
        db.session.commit()
        flash("Note deleted successfully", 'success')
        return redirect(url_for('notes'))
