from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/news')
def news():
    headlines = [
        {
            'title': 'Global Markets Rally as Inflation Cools',
            'datetime': datetime(2025, 7, 18, 9, 0),
            'category': 'Economy',
            'is_breaking': False
        },
        {
            'title': 'Major Earthquake Strikes Pacific Region',
            'datetime': datetime(2025, 7, 18, 8, 30),
            'category': 'World',
            'is_breaking': True
        },
        {
            'title': 'Tech Giants Release New AI Tools',
            'datetime': datetime(2025, 7, 17, 18, 45),
            'category': 'Technology',
            'is_breaking': False
        }
    ]
    return render_template('news.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)
