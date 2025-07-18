'''
16. Movie Picker
•	Dropdown list of genres in form
•	On submit, redirect to /movies/<genre>
•	Use request.form + redirect(url_for())
•	Display movie list via Jinja2
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample movies by genre
MOVIES = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
    "comedy": ["Superbad", "The Hangover", "Step Brothers"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"]
}

@app.route('/')
def home():
    genres = list(MOVIES.keys())
    return render_template('home.html', genres=genres)

@app.route('/pick', methods=['POST'])
def pick():
    genre = request.form.get('genre')
    if genre not in MOVIES:
        # fallback or error handling
        return redirect(url_for('home'))
    return redirect(url_for('movies', genre=genre))

@app.route('/movies/<genre>')
def movies(genre):
    genre = genre.lower()
    movies_list = MOVIES.get(genre)
    if not movies_list:
        return "Genre not found", 404
    return render_template('movies.html', genre=genre.title(), movies=movies_list)

if __name__ == '__main__':
    app.run(debug=True)
