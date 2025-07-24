from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Thread, Comment

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
                flash("Logged in successfully!", "success")
                return redirect(url_for('dashboard'))
            flash("Invalid username or password", "error")
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("You’ve been logged out.", "success")
        return redirect(url_for('login'))

    @app.route('/')
    @login_required
    def dashboard():
        threads = Thread.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', threads=threads)

    @app.route('/thread/new', methods=['GET', 'POST'])
    @login_required
    def new_thread():
        if request.method == 'POST':
            title = request.form['title']
            if not title.strip():
                flash("Title cannot be empty", "error")
                return redirect(url_for('new_thread'))
            thread = Thread(title=title, user_id=current_user.id)
            db.session.add(thread)
            db.session.commit()
            flash("Thread created!", "success")
            return redirect(url_for('dashboard'))
        return render_template('new_thread.html')

    @app.route('/thread/<int:thread_id>', methods=['GET', 'POST'])
    @login_required
    def thread(thread_id):
        thread = Thread.query.filter_by(id=thread_id, user_id=current_user.id).first_or_404()
        if request.method == 'POST':
            content = request.form['content']
            if not content.strip():
                flash("Comment cannot be empty", "error")
                return redirect(url_for('thread', thread_id=thread_id))
            comment = Comment(content=content, thread_id=thread_id, user_id=current_user.id)
            db.session.add(comment)
            db.session.commit()
            flash("Comment posted!", "success")
            return redirect(url_for('thread', thread_id=thread_id))
        comments = Comment.query.filter_by(thread_id=thread_id).all()
        return render_template('thread.html', thread=thread, comments=comments)
