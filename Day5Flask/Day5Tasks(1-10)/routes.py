from flask import Flask, request, jsonify
from app import app, db
from models import User

@app.route("/add_user", methods =['POST'])
def add_user():
    data = request.json
    new_user = User(
        username = data['username'],
        age = data['age']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(
        {
            "message": "User Added Successfully"
        }
    )

@app.route("/get_users", methods =['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        output.append(
            {
                'id' : user.id,
                'username' : user.username,
                "age" : user.age
            }
        )
    return jsonify(output)

@app.route('/update_user/<id>', methods =['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify(
            {
                "message" : "User not Found"
            }
        )
    data = request.json
    user.username = data.get('username', user.username)
    user.age = data.get('age', user.age)

    db.session.commit()

    return jsonify(
        {
            "message" : "User Updated Successfully"
        }
    )

@app.route('/delete_user/<id>', methods = ['DELETE'])
def delete_user(id):
    user= User.query.get(id)
    if not user:
        return jsonify(
            {
                "message" : "User not Found"
            }
        )
    db.session.delete(user)
    db.session.commit()

    return jsonify(
        {
            "message" : "User Deleted Successfully"
        }
    )