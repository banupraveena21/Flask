from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import User, Event, RSVP

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
        flash('Registration successful!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials', 'error')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash("Logged out.", "success")
    return redirect(url_for('main.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    rsvps = RSVP.query.filter_by(user_id=current_user.id).all()
    recent_event_id = session.get('recent_event_id')
    recent_event = Event.query.get(recent_event_id) if recent_event_id else None
    return render_template('dashboard.html', rsvps=rsvps, recent_event=recent_event)

@main.route('/events')
@login_required
def events():
    all_events = Event.query.all()
    return render_template('events.html', events=all_events)

@main.route('/rsvp/<int:event_id>', methods=['POST'])
@login_required
def rsvp(event_id):
    status = request.form['status']
    existing = RSVP.query.filter_by(user_id=current_user.id, event_id=event_id).first()
    if existing:
        existing.status = status
    else:
        new_rsvp = RSVP(status=status, user_id=current_user.id, event_id=event_id)
        db.session.add(new_rsvp)
    db.session.commit()
    session['recent_event_id'] = event_id
    flash('RSVP submitted!', 'success')
    return redirect(url_for('main.dashboard'))

@main.route('/rsvp/update/<int:rsvp_id>', methods=['GET', 'POST'])
@login_required
def update_rsvp(rsvp_id):
    rsvp = RSVP.query.get_or_404(rsvp_id)
    if request.method == 'POST':
        rsvp.status = request.form['status']
        db.session.commit()
        session['recent_event_id'] = rsvp.event_id
        flash("RSVP updated!", 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('update_rsvp.html', rsvp=rsvp)
