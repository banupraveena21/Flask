# 2. Online Book Showcase 
'''
Requirements: 
 /books route renders a list of books passed from Flask 
 Loop using {% for book in books %} to show cards with name & author 
 Use base.html for header/footer and inherit in books.html 
 Book cover images stored in static/images/
 Display message “No books available” using {% if %} 
'''

from flask import Flask, render_template

app = Flask(__name__)

# Sample book data
books = [
    {"name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "cover": "book.jpg"},
    {"name": "1984", "author": "George Orwell", "cover": "books.jpg"}
    
]

@app.route('/books')
def book_list():
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)