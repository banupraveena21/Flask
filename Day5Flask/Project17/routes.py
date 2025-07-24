
from flask import request, jsonify
from models import db, Post, Comment

def register_routes(app):
    @app.route('/posts', methods=['POST'])
    def create_post():
        data = request.get_json()
        post = Post(title=data['title'], content=data['content'])
        db.session.add(post)
        db.session.commit()
        return jsonify({'message': 'Post created successfully', 'post': post.to_dict()}), 201

    @app.route('/posts', methods=['GET'])
    def get_posts():
        posts = Post.query.all()
        return jsonify([p.to_dict() for p in posts])

    @app.route('/posts/<int:post_id>/comments', methods=['POST'])
    def add_comment(post_id):
        post = Post.query.get_or_404(post_id)
        data = request.get_json()
        comment = Comment(post_id=post.id, content=data['content'])
        db.session.add(comment)
        db.session.commit()
        return jsonify({'message': 'Comment added successfully', 'comment': comment.to_dict()}), 201

    @app.route('/posts/<int:post_id>/comments', methods=['GET'])
    def get_comments(post_id):
        post = Post.query.get_or_404(post_id)
        comments = Comment.query.filter_by(post_id=post.id).all()
        return jsonify([c.to_dict() for c in comments])
