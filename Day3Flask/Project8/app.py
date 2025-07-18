from flask import Flask, render_template

app = Flask(__name__)

@app.route('/blogs')
def blogs():
    blog_posts = [
        {
            'title': 'Understanding Flask Basics',
            'author': 'Alice Smith',
            'snippet': 'Flask is a lightweight WSGI web application framework...',
            'featured': True
        },
        {
            'title': 'Deep Dive into Jinja2',
            'author': 'Bob Johnson',
            'snippet': 'Jinja2 is a modern and designer-friendly templating language for Python...',
            'featured': False
        },
        {
            'title': 'Deploying Flask Apps',
            'author': 'Clara Lee',
            'snippet': 'Learn how to deploy Flask apps on various platforms...',
            'featured': True
        }
    ]
    return render_template('blogs.html', blogs=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
