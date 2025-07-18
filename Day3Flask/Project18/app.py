from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/event')
def event():
    event_name = "Product Launch"
    event_date = datetime(2025, 8, 1, 12, 0, 0)  # August 1, 2025 at 12:00 PM
    now = datetime.now()
    event_started = now >= event_date

    return render_template(
        "event.html",
        event_name=event_name,
        event_date=event_date.strftime('%Y-%m-%dT%H:%M:%S'),
        event_started=event_started
    )

if __name__ == '__main__':
    app.run(debug=True)
