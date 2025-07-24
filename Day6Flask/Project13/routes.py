from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Appointment

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
                flash("Username already taken", "error")
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
        flash("Logged out successfully.", "success")
        return redirect(url_for('login'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        appointments = Appointment.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', appointments=appointments)

    @app.route('/book', methods=['GET', 'POST'])
    @login_required
    def book():
        if request.method == 'POST':
            date = request.form['date']
            time = request.form['time']
            appointment = Appointment(date=date, time=time, user_id=current_user.id)
            db.session.add(appointment)
            db.session.commit()
            flash("Appointment booked!", "success")
            return redirect(url_for('dashboard'))
        return render_template('book.html')

    @app.route('/update/<int:appointment_id>', methods=['GET', 'POST'])
    @login_required
    def update(appointment_id):
        appointment = Appointment.query.get_or_404(appointment_id)
        if appointment.user_id != current_user.id:
            flash("Unauthorized access!", "error")
            return redirect(url_for('dashboard'))
        if request.method == 'POST':
            appointment.date = request.form['date']
            appointment.time = request.form['time']
            appointment.status = request.form.get('status', appointment.status)
            db.session.commit()
            flash("Appointment updated!", "success")
            return redirect(url_for('dashboard'))
        return render_template('update.html', appointment=appointment)

    @app.route('/cancel/<int:appointment_id>')
    @login_required
    def cancel(appointment_id):
        appointment = Appointment.query.get_or_404(appointment_id)
        if appointment.user_id != current_user.id:
            flash("Unauthorized access!", "error")
            return redirect(url_for('dashboard'))
        appointment.status = 'Cancelled'
        db.session.commit()
        flash("Appointment cancelled.", "success")
        return redirect(url_for('dashboard'))
