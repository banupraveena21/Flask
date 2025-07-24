from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import User
from forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)

import logging
logging.basicConfig(level=logging.INFO, filename='auth.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

@main.route('/')
def index():
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            session['login_count'] = session.get('login_count', 0) + 1
            session['last_login'] = str(user.id)  # Can store actual datetime if needed
            flash(f'Welcome back, {user.username}!', 'success')
            logging.info(f"User {user.email} logged in successfully.")
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password.', 'error')
            logging.warning(f"Failed login attempt for email: {form.email.data}")
    return render_template('login.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/settings')
@login_required
def settings():
    last_login = session.get('last_login', 'Unknown')
    login_count = session.get('login_count', 0)
    return render_template('settings.html', last_login=last_login, login_count=login_count)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.login'))
