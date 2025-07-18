'''
13. News Category Reader
•	Route: /news/<category>
•	Display hardcoded news from list
•	Reuse layout with extends and {% block content %}
'''

from flask import Flask, render_template, abort

app = Flask(__name__)

NEWS_DATA = {
    "technology": [
        "Tech company launches new AI tool.",
        "Breakthrough in quantum computing announced.",
        "New smartphone model released with innovative features."
    ],
    "sports": [
        "Local team wins championship.",
        "Star player breaks scoring record.",
        "Upcoming sports events this weekend."
    ],
    "politics": [
        "Government passes new reform bill.",
        "Election results announced.",
        "International summit scheduled next month."
    ]
}

@app.route('/')
def home():
    categories = list(NEWS_DATA.keys())
    return render_template('home.html', categories=categories)

@app.route('/news/<category>')
def news(category):
    category = category.lower()
    if category not in NEWS_DATA:
        abort(404)
    articles = NEWS_DATA[category]
    return render_template('news.html', category=category.title(), articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
