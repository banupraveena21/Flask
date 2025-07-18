from flask import Flask, render_template

app = Flask(__name__)

@app.route('/team')
def team():
    team_members = [
        {
            'name': 'Alice Johnson',
            'role': 'Team Lead',
            'photo': 'alice.jpg'
        },
        {
            'name': 'Bob Smith',
            'role': 'Backend Developer',
            'photo': 'bob.jpg'
        },
        {
            'name': 'Clara Lee',
            'role': 'UI/UX Designer',
            'photo': 'clara.jpg'
        }
    ]
    return render_template('team.html', team=team_members)

if __name__ == '__main__':
    app.run(debug=True)
