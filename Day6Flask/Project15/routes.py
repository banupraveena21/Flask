from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Feedback

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
            flash("Registered successfully", "success")
            return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user and user.check_password(request.form['password']):
                login_user(user)
                flash("Welcome!", "success")
                return redirect(url_for('feedback'))
            flash("Invalid credentials", "error")
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("Logged out", "success")
        return redirect(url_for('login'))

    @app.route('/feedback', methods=['GET', 'POST'])
    @login_required
    def feedback():
        if request.method == 'POST':
            comment = request.form['comment']
            fb = Feedback(user_name=current_user.username, comment=comment)
            db.session.add(fb)
            db.session.commit()
            flash("Thank you for your feedback!", "success")
            return redirect(url_for('feedback'))
        return render_template('feedback.html')

    @app.route('/admin')
    @login_required
    def admin():
        if not current_user.is_admin:
            flash("Access denied.", "error")
            return redirect(url_for('feedback'))
        all_feedback = Feedback.query.all()
        return render_template('admin.html', feedbacks=all_feedback)
