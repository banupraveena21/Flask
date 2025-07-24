
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, QuizResult

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
            flash("Registration successful. Please log in.", 'success')
            return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user and user.check_password(request.form['password']):
                login_user(user)
                flash("Login successful", 'success')
                return redirect(url_for('dashboard'))
            flash("Invalid credentials", 'error')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("Logged out successfully", 'success')
        return redirect(url_for('login'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        scores = QuizResult.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', scores=scores)

    @app.route('/quiz', methods=['GET', 'POST'])
    @login_required
    def quiz():
        questions = {
            "What is 2 + 2?": "4",
            "What is capital of France?": "Paris",
            "Who developed Python?": "Guido"
        }
        if request.method == 'POST':
            score = 0
            for q, correct in questions.items():
                answer = request.form.get(q, "").strip()
                if answer.lower() == correct.lower():
                    score += 1
            result = QuizResult(score=score, total=len(questions), user_id=current_user.id)
            db.session.add(result)
            db.session.commit()
            flash("Quiz completed!", 'success')
            return redirect(url_for('results'))
        return render_template('quiz.html', questions=questions)

    @app.route('/results')
    @login_required
    def results():
        last_result = QuizResult.query.filter_by(user_id=current_user.id).order_by(QuizResult.id.desc()).first()
        return render_template('results.html', result=last_result)
