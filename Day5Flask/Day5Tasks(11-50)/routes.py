from flask import request, jsonify
from app import app, db
from models import Users, Product, Blog, Category, Review

# 1. Create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user = Users(name=data['name'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# 2. Create new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created'}), 201

# 3. Create blog post
@app.route('/blogs', methods=['POST'])
def create_blog():
    data = request.get_json()
    blog = Blog(title=data['title'], content=data['content'])
    db.session.add(blog)
    db.session.commit()
    return jsonify({'message': 'Blog post created'}), 201

# 4. Add dummy data
@app.route('/dummy', methods=['POST'])
def add_dummy():
    user = Users(name="Test", email="test@test.com")
    product = Product(name="Demo", price=100.0)
    db.session.add_all([user, product])
    db.session.commit()
    return jsonify({'message': 'Dummy data inserted'})

# 5. Bulk insert
@app.route('/bulk/products', methods=['POST'])
def bulk_products():
    items = [Product(name=f"Item {i}", price=10*i) for i in range(1, 6)]
    db.session.add_all(items)
    db.session.commit()
    return jsonify({'message': '5 Products inserted'})

# 6. Handle duplicate email
@app.route('/test-email', methods=['POST'])
def test_email():
    try:
        user = Users(name="Dup", email="test@test.com")
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User added'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Email already exists'})

# 7. Read all users
@app.route('/users', methods=['GET'])
def list_users():
    users = Users.query.all()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users])

# 8. Read single user
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = Users.query.get_or_404(id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

# 9. Filter by email
@app.route('/users/email/<email>', methods=['GET'])
def get_by_email(email):
    user = Users.query.filter_by(email=email).first()
    return jsonify({'id': user.id, 'name': user.name}) if user else (jsonify({'error': 'Not found'}), 404)

# 10. Products in stock
@app.route('/products/in-stock', methods=['GET'])
def get_stocked():
    products = Product.query.filter_by(in_stock=True).all()
    return jsonify([{'name': p.name, 'price': p.price} for p in products])

# 11. Blogs descending
@app.route('/blogs', methods=['GET'])
def get_blogs():
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return jsonify([{'title': b.title, 'created_at': b.created_at.isoformat()} for b in blogs])

# 12. Count users
@app.route('/users/count', methods=['GET'])
def count_users():
    return jsonify({'total': Users.query.count()})

# 13. Update user info
@app.route('/api/user/<int:id>', methods=['PUT'])
def update_user(id):
    user = Users.query.get_or_404(id)
    data = request.get_json()
    before = {'name': user.name, 'email': user.email}
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({'message': 'User updated', 'before': before, 'after': {'name': user.name, 'email': user.email}})

# 14. Update product stock
@app.route('/product/<int:id>/stock', methods=['PUT'])
def update_stock(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.in_stock = data.get('in_stock', True)
    db.session.commit()
    return jsonify({'message': 'Stock updated'})

# 15. Simulate password change (for example)
@app.route('/users/<int:id>/password', methods=['PUT'])
def change_password(id):
    user = Users.query.get_or_404(id)
    data = request.get_json()
    if data.get('current_password') == 'oldpass':
        return jsonify({'message': 'Password changed (mocked)'})
    return jsonify({'error': 'Invalid current password'}), 403
