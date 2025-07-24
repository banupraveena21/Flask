from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Book

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
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                flash("Login successful!", "success")
                return redirect(url_for('books'))
            flash("Invalid credentials", "error")
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        session.pop('last_viewed_book', None)
        flash("Logged out", "info")
        return redirect(url_for('login'))

    @app.route('/books')
    @login_required
    def books():
        books = Book.query.filter_by(user_id=current_user.id).all()
        last_book_id = session.get('last_viewed_book')
        return render_template('books.html', books=books, last_book_id=last_book_id)

    @app.route('/add', methods=['GET', 'POST'])
    @login_required
    def add():
        if request.method == 'POST':
            title = request.form['title']
            total_pages = int(request.form['total_pages'])
            book = Book(title=title, total_pages=total_pages, user_id=current_user.id)
            db.session.add(book)
            db.session.commit()
            flash("Book added!", "success")
            return redirect(url_for('books'))
        return render_template('add_book.html')

    @app.route('/update/<int:book_id>', methods=['GET', 'POST'])
    @login_required
    def update(book_id):
        book = Book.query.get_or_404(book_id)
        if book.user_id != current_user.id:
            flash("Unauthorized", "error")
            return redirect(url_for('books'))
        session['last_viewed_book'] = book.id
        if request.method == 'POST':
            book.pages_read = int(request.form['pages_read'])
            db.session.commit()
            flash("Progress updated!", "success")
            return redirect(url_for('books'))
        return render_template('update_book.html', book=book)
