'''
10. City Weather Display (Static Simulation)
•	Route /weather/<city>?unit=celsius
•	Return static weather data styled with weather icons (from static/images)
•	Use {% if %} to change icons based on weather
'''

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


STATIC_WEATHER = {
    'london': {'temp_c': 18, 'temp_f': 64, 'condition': 'cloudy'},
    'dubai': {'temp_c': 38, 'temp_f': 100, 'condition': 'sunny'},
    'moscow': {'temp_c': -5, 'temp_f': 23, 'condition': 'snow'},
    'mumbai': {'temp_c': 30, 'temp_f': 86, 'condition': 'rain'},
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        unit = request.form.get('unit', 'celsius')
        if city:
            return redirect(url_for('weather', city=city, unit=unit))
    return render_template('home.html')

@app.route('/weather/<city>')
def weather(city):
    unit = request.args.get('unit', 'celsius').lower()
    city_lower = city.lower()
    weather_data = STATIC_WEATHER.get(city_lower)

    if not weather_data:
        return f"<h1>No weather data available for '{city}'</h1>"

    temp = weather_data['temp_c'] if unit == 'celsius' else weather_data['temp_f']
    condition = weather_data['condition']

    return render_template('weather.html', city=city.title(), temp=temp, unit=unit, condition=condition)

if __name__ == '__main__':
    app.run(debug=True)
