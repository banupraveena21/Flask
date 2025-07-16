# 13. Book Recommendation System
'''
Requirements:
- /recommend: GET form with genre (sci-fi, romance)
- POST to /show-recommendation
- Redirect to /thanks/<user>
- /books?genre=sci-fi to filter results
- Use request.form and dynamic /book/<title> route
'''


from flask import Flask, request, redirect, url_for

app = Flask(__name__)


books = [
    {"title": "Dune", "genre": "sci-fi", "description": "A classic sci-fi epic."},
    {"title": "Neuromancer", "genre": "sci-fi", "description": "Cyberpunk at its finest."},
    {"title": "Pride and Prejudice", "genre": "romance", "description": "Timeless romantic tale."},
    {"title": "The Notebook", "genre": "romance", "description": "Heartfelt modern romance."}
]


last_user = ""


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        global last_user
        genre = request.form.get('genre')
        user = request.form.get('user')
        last_user = user
        return redirect(url_for('show_recommendation'))

    return '''
    <h2>Book Recommendation</h2>
    <form method="POST">
        Your Name: <input type="text" name="user" required><br><br>
        Select Genre:
        <select name="genre" required>
            <option value="sci-fi">Sci-Fi</option>
            <option value="romance">Romance</option>
        </select><br><br>
        <input type="submit" value="Get Recommendation">
    </form>
    '''


@app.route('/show-recommendation')
def show_recommendation():
    global last_user
    
    return redirect(url_for('thanks', user=last_user))


@app.route('/thanks/<user>')
def thanks(user):
    return f"<h3>Thanks, {user.title()}! We've shared some book recommendations based on your taste.</h3>"


@app.route('/books')
def list_books():
    genre = request.args.get('genre')
    filtered = books if not genre else [b for b in books if b['genre'] == genre.lower()]

    if not filtered:
        return f"<p>No books found for genre: <strong>{genre}</strong></p>"

    html = f"<h3>Books in Genre: {genre.title()}</h3><ul>"
    for book in filtered:
        html += f'<li><a href="/book/{book["title"].replace(" ", "-")}">{book["title"]}</a></li>'
    html += "</ul>"
    return html


@app.route('/book/<title>')
def book_detail(title):
    
    title_clean = title.replace("-", " ").lower()
    book = next((b for b in books if b['title'].lower() == title_clean), None)
    if not book:
        return f"<h3>Book '{title}' not found.</h3>", 404

    return f'''
    <h2>{book["title"]}</h2>
    <p><strong>Genre:</strong> {book["genre"].title()}</p>
    <p><strong>Description:</strong> {book["description"]}</p>
    '''


if __name__ == '__main__':
    app.run(debug=True)