from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/achievements')
def achievements():
    data = {
        2025: [
            "Launched AI-powered dashboard",
            "Won National Innovation Award"
        ],
        2024: [
            "Expanded to 3 new countries",
            "Reached 1 million users"
        ],
        2023: [
            "Secured Series B funding",
            "Opened new HQ in Berlin"
        ]
    }

    current_year = datetime.now().year
    return render_template('achievements.html', data=data, current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True)
