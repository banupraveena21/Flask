
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from models import db, User, Review

def register_routes(app, login_manager):
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def index():
        reviews = Review.query.all()
        return render_template('index.html', reviews=reviews)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if User.query.filter_by(username=username).first():
                flash("Username already taken", 'error')
                return redirect(url_for('register'))
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash("Registration successful", 'success')
            return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user and user.check_password(request.form['password']):
                login_user(user)
                flash("Login successful", 'success')
                return redirect(url_for('index'))
            flash("Invalid credentials", 'error')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("Logged out successfully", 'success')
        return redirect(url_for('index'))

    @app.route('/review/add', methods=['GET', 'POST'])
    @login_required
    def add_review():
        if request.method == 'POST':
            movie = request.form['movie']
            rating = int(request.form['rating'])
            comment = request.form['comment']
            review = Review(movie=movie, rating=rating, comment=comment, user_id=current_user.id)
            db.session.add(review)
            db.session.commit()
            flash("Review submitted!", 'success')
            return redirect(url_for('index'))
        return render_template('add_review.html')
