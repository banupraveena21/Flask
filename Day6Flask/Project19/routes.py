from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import User, JournalEntry

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'error')
            return redirect(url_for('main.register'))
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully! Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('main.journal'))
        flash('Invalid username or password', 'error')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for('main.login'))

@main.route('/journal')
@login_required
def journal():
    entries = JournalEntry.query.filter_by(user_id=current_user.id).all()
    return render_template('journal.html', entries=entries)

@main.route('/journal/add', methods=['GET', 'POST'])
@login_required
def add_entry():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        entry = JournalEntry(title=title, content=content, user_id=current_user.id)
        db.session.add(entry)
        db.session.commit()
        flash('Entry added successfully!', 'success')
        return redirect(url_for('main.journal'))
    return render_template('add_entry.html')

@main.route('/journal/update/<int:entry_id>', methods=['GET', 'POST'])
@login_required
def update_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    if entry.author != current_user:
        flash('Access denied!', 'error')
        return redirect(url_for('main.journal'))

    if request.method == 'POST':
        entry.title = request.form['title']
        entry.content = request.form['content']
        db.session.commit()
        flash('Entry updated successfully!', 'success')
        return redirect(url_for('main.journal'))
    return render_template('update_entry.html', entry=entry)

@main.route('/journal/delete/<int:entry_id>', methods=['POST'])
@login_required
def delete_entry(entry_id):
    entry = JournalEntry.query.get_or_404(entry_id)
    if entry.author != current_user:
        flash('Access denied!', 'error')
        return redirect(url_for('main.journal'))
    db.session.delete(entry)
    db.session.commit()
    flash('Entry deleted successfully!', 'success')
    return redirect(url_for('main.journal'))
