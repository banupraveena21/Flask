from flask import request, jsonify, abort
from app import app, db  
from models import Post

# Create a blog post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or not all(k in data for k in ['title', 'content', 'author']):
        return jsonify({"error": "Missing required fields"}), 400

    post = Post(title=data['title'], content=data['content'], author=data['author'])
    db.session.add(post)
    db.session.commit()
    return jsonify({"message": "Post created successfully", "post": post.to_dict()}), 201

# Get all posts
@app.route('/posts', methods=['GET'])
def get_all_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([p.to_dict() for p in posts]), 200

# Update a post
@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    post.author = data.get('author', post.author)
    db.session.commit()
    return jsonify({"message": "Post updated successfully", "post": post.to_dict()}), 200

# Delete a post
@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully"}), 200
