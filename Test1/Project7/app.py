from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def color_picker():
    default_color = "#c2db34" 
    color = default_color

    if request.method == 'POST':
        input_color = request.form.get('color', '').strip()
        if input_color:
            color = input_color

    return render_template('color_picker.html', color=color)

if __name__ == '__main__':
    app.run(debug=True)
