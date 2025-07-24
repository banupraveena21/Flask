from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, JournalEntry

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
                session['login_time'] = request.environ.get('HTTP_DATE') or 'Now'
                flash("Logged in successfully", "success")
                return redirect(url_for('dashboard'))
            flash("Invalid credentials", "error")
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        session.clear()
        flash("Logged out", "success")
        return redirect(url_for('login'))

    @app.route('/')
    @login_required
    def dashboard():
        entries = JournalEntry.query.filter_by(user_id=current_user.id).all()
        login_time = session.get('login_time', 'N/A')
        return render_template('dashboard.html', entries=entries, login_time=login_time)

    @app.route('/add', methods=['GET', 'POST'])
    @login_required
    def add_entry():
        if request.method == 'POST':
            entry = JournalEntry(
                title=request.form['title'],
                content=request.form['content'],
                user_id=current_user.id
            )
            db.session.add(entry)
            db.session.commit()
            flash("Entry added", "success")
            return redirect(url_for('dashboard'))
        return render_template('journal_form.html', action="Add")

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    @login_required
    def edit_entry(id):
        entry = JournalEntry.query.get_or_404(id)
        if entry.user_id != current_user.id:
            flash("Unauthorized", "error")
            return redirect(url_for('dashboard'))
        if request.method == 'POST':
            entry.title = request.form['title']
            entry.content = request.form['content']
            db.session.commit()
            flash("Entry updated", "success")
            return redirect(url_for('dashboard'))
        return render_template('journal_form.html', action="Edit", entry=entry)

    @app.route('/delete/<int:id>')
    @login_required
    def delete_entry(id):
        entry = JournalEntry.query.get_or_404(id)
        if entry.user_id == current_user.id:
            db.session.delete(entry)
            db.session.commit()
            flash("Entry deleted", "success")
        else:
            flash("Unauthorized", "error")
        return redirect(url_for('dashboard'))
