# routes.py

from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from models import db, User, Workout

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
            flash("Registered successfully", 'success')
            return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user and user.check_password(request.form['password']):
                login_user(user)
                flash("Welcome back!", 'success')
                return redirect(url_for('dashboard'))
            flash("Invalid credentials", 'error')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("Logged out successfully", 'success')
        return redirect(url_for('login'))

    @app.route('/dashboard', methods=['GET', 'POST'])
    @login_required
    def dashboard():
        if request.method == 'POST':
            workout_type = request.form['type']
            steps = int(request.form['steps'])
            duration = float(request.form['duration'])
            session['last_type'] = workout_type  # remember last type
            workout = Workout(type=workout_type, steps=steps, duration=duration, user_id=current_user.id)
            db.session.add(workout)
            db.session.commit()
            flash("Workout logged!", 'success')
            return redirect(url_for('dashboard'))

        last_type = session.get('last_type', '')
        return render_template('dashboard.html', last_type=last_type)

    @app.route('/history')
    @login_required
    def history():
        workouts = Workout.query.filter_by(user_id=current_user.id).order_by(Workout.date.desc()).all()
        return render_template('history.html', workouts=workouts)

    @app.route('/profile', methods=['GET', 'POST'])
    @login_required
    def profile():
        if request.method == 'POST':
            current_pwd = request.form['current_password']
            new_pwd = request.form['new_password']
            if not current_user.check_password(current_pwd):
                flash("Incorrect current password", 'error')
                return redirect(url_for('profile'))
            current_user.set_password(new_pwd)
            db.session.commit()
            flash("Password updated", 'success')
            return redirect(url_for('profile'))
        return render_template('profile.html')
