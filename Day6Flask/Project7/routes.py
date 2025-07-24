from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Bug

def register_routes(app, login_manager):
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def home():
        return redirect(url_for('dashboard'))

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
                flash("Logged in!", 'success')
                return redirect(url_for('dashboard'))
            flash("Invalid credentials", 'error')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("Logged out", 'success')
        return redirect(url_for('login'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        bugs = Bug.query.filter_by(user_id=current_user.id).all()
        last_title = session.get('last_bug_title')
        return render_template('dashboard.html', bugs=bugs, last_title=last_title)

    @app.route('/report', methods=['GET', 'POST'])
    @login_required
    def report():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            bug = Bug(title=title, description=description, user_id=current_user.id)
            db.session.add(bug)
            db.session.commit()
            session['last_bug_title'] = title
            flash("Bug reported!", 'success')
            return redirect(url_for('dashboard'))
        return render_template('report.html')
