from flask import request, jsonify
from app import app, db
from models import Product

# Add a product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or not all(k in data for k in ['name', 'price', 'description']):
        return jsonify({'error': 'Missing fields'}), 400

    product = Product(
        name=data['name'],
        price=data['price'],
        in_stock=data.get('in_stock', True),
        description=data['description']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added', 'product': product.to_dict()}), 201

# View all products
@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products]), 200

# View in-stock products only
@app.route('/products/in-stock', methods=['GET'])
def get_in_stock_products():
    products = Product.query.filter_by(in_stock=True).all()
    return jsonify([p.to_dict() for p in products]), 200

# Update a product
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.in_stock = data.get('in_stock', product.in_stock)
    product.description = data.get('description', product.description)
    db.session.commit()
    return jsonify({'message': 'Product updated', 'product': product.to_dict()}), 200

# Delete a product
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 200
