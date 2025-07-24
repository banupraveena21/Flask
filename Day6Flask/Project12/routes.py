from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from models import db, User, Book, Borrow

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
                flash("Username exists!", "error")
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
                return redirect(url_for('dashboard'))
            flash("Invalid username or password", "error")
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        session.pop('recent_borrowed', None)
        flash("Logged out.", "success")
        return redirect(url_for('login'))

    @app.route('/')
    @login_required
    def dashboard():
        books = Book.query.filter_by(available=True).all()
        recent = session.get('recent_borrowed', [])
        return render_template('dashboard.html', books=books, recent=recent)

    @app.route('/borrow/<int:book_id>')
    @login_required
    def borrow(book_id):
        book = Book.query.get_or_404(book_id)
        if not book.available:
            flash("Book already borrowed", "error")
            return redirect(url_for('dashboard'))

        # Create borrow record
        borrow = Borrow(user_id=current_user.id, book_id=book.id, borrow_date=datetime.utcnow())
        book.available = False
        db.session.add(borrow)
        db.session.commit()

        # Update session for recently borrowed
        recent = session.get('recent_borrowed', [])
        recent.insert(0, book.title)
        session['recent_borrowed'] = recent[:5]  # keep last 5 borrowed

        flash(f"You borrowed '{book.title}'", "success")
        return redirect(url_for('dashboard'))

    # Optional admin view
    @app.route('/admin/borrowed')
    @login_required
    def admin_borrowed():
        if not current_user.is_admin:
            flash("Access denied", "error")
            return redirect(url_for('dashboard'))
        borrowings = Borrow.query.order_by(Borrow.borrow_date.desc()).all()
        return render_template('admin.html', borrowings=borrowings)
