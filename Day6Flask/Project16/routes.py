from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Application

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
                flash("Logged in successfully!", "success")
                return redirect(url_for('apply'))
            flash("Invalid credentials", "error")
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("Logged out", "success")
        return redirect(url_for('login'))

    @app.route('/apply', methods=['GET', 'POST'])
    @login_required
    def apply():
        if request.method == 'POST':
            job_title = request.form['job_title']
            resume_text = request.form['resume_text']
            application = Application(job_title=job_title, resume_text=resume_text, user_id=current_user.id)
            db.session.add(application)
            db.session.commit()
            flash("Application submitted successfully!", "success")
            return redirect(url_for('my_applications'))
        return render_template('apply.html')

    @app.route('/my-applications')
    @login_required
    def my_applications():
        applications = Application.query.filter_by(user_id=current_user.id).all()
        return render_template('my_applications.html', applications=applications)
