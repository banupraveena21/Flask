# 4. Daily Weather Report 
'''
 Requirements: 
 /weather renders today’s weather info sent from Flask 
 Show icons (sun, rain) from static/images/ 
 Use {% if temperature > 30 %} to suggest “Stay Hydrated” 
 Include a temperature chart using JS from static/script.js 
 Extend from a common layout'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/weather')
def weather():
    weather_data = {
        'city': 'New York',
        'condition': 'Sunny',
        'temperature': 33,
        'icon': 'sun.png',
        'week_temps': [30, 32, 33, 31, 29, 28, 27]
    }
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
