from flask import request, jsonify
from app import app, db
from models import Book

# Add new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not all(k in data for k in ['title', 'author', 'quantity', 'published_year']):
        return jsonify({'error': 'Missing required fields'}), 400

    book = Book(**data)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book added', 'book': book.to_dict()}), 201

# Get all books sorted by published year
@app.route('/books', methods=['GET'])
def list_books():
    books = Book.query.order_by(Book.published_year.asc()).all()
    return jsonify([b.to_dict() for b in books]), 200

# Update book quantity
@app.route('/books/<int:id>', methods=['PUT'])
def update_quantity(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    if 'quantity' in data:
        book.quantity = data['quantity']
        db.session.commit()
        return jsonify({'message': 'Quantity updated', 'book': book.to_dict()}), 200
    return jsonify({'error': 'Quantity field required'}), 400

# Delete book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'}), 200
