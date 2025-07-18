from flask import Flask, render_template

app = Flask(__name__)

@app.route('/testimonials')
def testimonials():
    feedbacks = [
        {
            'name': 'Alice Johnson',
            'comment': 'Amazing service, will definitely come back!',
            'photo': 'user1.jpg',
            'rating': 5
        },
        {
            'name': 'Bob Smith',
            'comment': 'Good experience, but room for improvement.',
            'photo': 'user2.jpg',
            'rating': 3
        },
        {
            'name': 'Clara Lee',
            'comment': 'Customer support was very helpful.',
            'photo': 'user3.jpg',
            'rating': 4
        }
    ]
    return render_template('testimonials.html', testimonials=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
