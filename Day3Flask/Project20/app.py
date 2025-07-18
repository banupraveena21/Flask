from flask import Flask, render_template

app = Flask(__name__)

@app.route('/leaderboard')
def leaderboard():
    leaderboard = [
        {"name": "Alice", "score": 980},
        {"name": "Bob", "score": 870},
        {"name": "Charlie", "score": 850},
        {"name": "Diana", "score": 830},
        {"name": "Eve", "score": 800},
    ]
    return render_template("leaderboard.html", leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
