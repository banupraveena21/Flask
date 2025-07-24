from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Plan

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
                flash("Username already exists", "error")
                return redirect(url_for('register'))
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash("Registration successful!", "success")
            return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user and user.check_password(request.form['password']):
                login_user(user)
                flash("Logged in!", "success")
                return redirect(url_for('dashboard'))
            flash("Invalid credentials", "error")
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        session.pop('last_search', None)
        flash("Logged out", "success")
        return redirect(url_for('login'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        plans = Plan.query.filter_by(user_id=current_user.id).all()
        total = len(plans)
        return render_template('dashboard.html', plans=plans, total=total, last=session.get('last_search'))

    @app.route('/add', methods=['GET', 'POST'])
    @login_required
    def add():
        if request.method == 'POST':
            place = request.form['place']
            date = request.form['date']
            reason = request.form['reason']
            session['last_search'] = place  # Store last searched place
            plan = Plan(place=place, date=date, reason=reason, user_id=current_user.id)
            db.session.add(plan)
            db.session.commit()
            flash("Travel plan added!", "success")
            return redirect(url_for('dashboard'))
        return render_template('add_plan.html')
