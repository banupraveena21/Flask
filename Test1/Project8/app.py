'''
8. Book Recommendation Page
•	Form with favorite genre
•	Redirect to /books/<genre>
•	Show recommended books using Jinja2 loop
•	Genre comes from route param
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for book recommendations
BOOKS_BY_GENRE = {
    'fantasy': [
        'The Hobbit by J.R.R. Tolkien',
        'Harry Potter and the Sorcerer\'s Stone by J.K. Rowling',
        'A Game of Thrones by George R.R. Martin'
    ],
    'science-fiction': [
        'Dune by Frank Herbert',
        'Neuromancer by William Gibson',
        'Ender\'s Game by Orson Scott Card'
    ],
    'mystery': [
        'The Girl with the Dragon Tattoo by Stieg Larsson',
        'Gone Girl by Gillian Flynn',
        'Sherlock Holmes by Arthur Conan Doyle'
    ],
    'romance': [
        'Pride and Prejudice by Jane Austen',
        'Me Before You by Jojo Moyes',
        'Outlander by Diana Gabaldon'
    ]
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        genre = request.form.get('genre', '').lower().replace(' ', '-')
        return redirect(url_for('books', genre=genre))
    return render_template('home.html')

@app.route('/books/<genre>')
def books(genre):
    books = BOOKS_BY_GENRE.get(genre, [])
    return render_template('books.html', genre=genre.replace('-', ' ').title(), books=books)

if __name__ == '__main__':
    app.run(debug=True)
