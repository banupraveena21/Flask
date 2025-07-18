from flask import Flask, render_template

app = Flask(__name__)

@app.route('/menu')
def menu():
    menu_data = {
        'Starter': [
            {'name': 'Bruschetta', 'price': 6.5, 'available': True, 'image': 'bruschetta.jpg'},
            {'name': 'Stuffed Mushrooms', 'price': 7.0, 'available': False, 'image': 'stuffedmushrooms.jpg'}
        ],
        'Main': [
            {'name': 'Grilled Ribeye Steak', 'price': 25.0, 'available': True, 'image': 'steak.jpg'},
            {'name': 'Seared Salmon', 'price': 22.5, 'available': True, 'image': 'salmon.jpg'}
        ],
        'Dessert': [
            {'name': 'Cheesecake', 'price': 8.0, 'available': False, 'image': 'cheesecake.jpg'},
            {'name': 'Tiramisu', 'price': 7.5, 'available': True, 'image': 'tiramisu.jpg'}
        ]
    }
    return render_template('menu.html', menu=menu_data)

if __name__ == '__main__':
    app.run(debug=True)
