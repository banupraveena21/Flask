'''
4. Budget Manager 
 Features: 
 Logged-in users can add expenses (amount, category). 
 View expense summary per user. 
 Use session to store monthly spending limit. 
 Flash warning when expenses cross limit.
'''

from flask import Flask, render_template, request, redirect, session, flash, url_for
from models import db, User, Expense
from config import Config
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()

# Register dummy user for testing
@app.route('/register')
def register():
    if not User.query.filter_by(username='testuser').first():
        hashed = generate_password_hash('password', method='sha256')
        user = User(username='testuser', password=hashed)
        db.session.add(user)
        db.session.commit()
    return 'User created: testuser / password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        session['limit'] = float(request.form['limit'])
        flash('Monthly limit set successfully!', 'success')
        return redirect(url_for('dashboard'))

    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    total = sum(e.amount for e in expenses)
    limit = session.get('limit', 0)

    if limit and total > limit:
        flash('⚠️ You have exceeded your monthly spending limit!', 'error')

    return render_template('dashboard.html', expenses=expenses, total=total, limit=limit)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_expense():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        expense = Expense(user_id=current_user.id, amount=amount, category=category)
        db.session.add(expense)
        db.session.commit()
        flash('Expense added!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_expense.html')


