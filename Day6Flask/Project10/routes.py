from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Course, Enrollment

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
            flash("Registered successfully!", "success")
            return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user and user.check_password(request.form['password']):
                login_user(user)
                flash("Login successful", "success")
                return redirect(url_for('courses'))
            flash("Invalid credentials", "error")
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("Logged out", "success")
        return redirect(url_for('login'))

    @app.route('/courses')
    @login_required
    def courses():
        available_courses = Course.query.all()
        return render_template('courses.html', courses=available_courses)

    @app.route('/enroll/<int:course_id>')
    @login_required
    def enroll(course_id):
        existing = Enrollment.query.filter_by(user_id=current_user.id, course_id=course_id).first()
        if not existing:
            enrollment = Enrollment(user_id=current_user.id, course_id=course_id)
            db.session.add(enrollment)
            db.session.commit()
            flash("Enrolled successfully!", "success")
        else:
            flash("Already enrolled in this course.", "info")
        return redirect(url_for('history'))

    @app.route('/history')
    @login_required
    def history():
        enrollments = Enrollment.query.filter_by(user_id=current_user.id).all()
        return render_template('history.html', enrollments=enrollments)
