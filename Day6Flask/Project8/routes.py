from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, Admin, Product

def is_admin():
    return current_user.is_authenticated

def register_routes(app, login_manager):
    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            admin = Admin.query.filter_by(email=request.form['email']).first()
            if admin and admin.check_password(request.form['password']):
                login_user(admin)
                flash("Logged in as admin", "success")
                return redirect(url_for('dashboard'))
            flash("Invalid login", "error")
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("Logged out", "success")
        return redirect(url_for('login'))

    @app.route('/')
    @login_required
    def dashboard():
        products = Product.query.all()
        return render_template('dashboard.html', products=products)

    @app.route('/add', methods=['GET', 'POST'])
    @login_required
    def add_product():
        if request.method == 'POST':
            p = Product(
                name=request.form['name'],
                price=float(request.form['price']),
                stock=int(request.form['stock'])
            )
            db.session.add(p)
            db.session.commit()
            flash("Product added", "success")
            return redirect(url_for('dashboard'))
        return render_template('product_form.html', action="Add")

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    @login_required
    def edit_product(id):
        product = Product.query.get_or_404(id)
        if request.method == 'POST':
            product.name = request.form['name']
            product.price = float(request.form['price'])
            product.stock = int(request.form['stock'])
            db.session.commit()
            flash("Product updated", "success")
            return redirect(url_for('dashboard'))
        return render_template('product_form.html', action="Edit", product=product)

    @app.route('/delete/<int:id>')
    @login_required
    def delete_product(id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        flash("Product deleted", "success")
        return redirect(url_for('dashboard'))
