from flask import Flask, render_template, abort
from datetime import datetime, timedelta

app = Flask(__name__)

users = {
    "alice": {
        "name": "Alice Johnson",
        "bio": "Full-stack developer and open source enthusiast.",
        "joined": datetime.now() - timedelta(days=3),
        "image": "alice.jpg"
    },
    "bob": {
        "name": "Bob Smith",
        "bio": "UX designer with a love for simplicity.",
        "joined": datetime.now() - timedelta(days=30),
        "image": "bob.jpg"
    }
}

@app.route('/profile/<username>')
def profile(username):
    user = users.get(username)
    if not user:
        abort(404)

    is_new = (datetime.now() - user["joined"]).days < 7

    return render_template(
        "profile.html",
        user=user,
        is_new=is_new
    )

if __name__ == '__main__':
    app.run(debug=True)
