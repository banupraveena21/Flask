from flask import Flask, render_template

app = Flask(__name__)

@app.route('/products')
def products():
    product_list = [
        {
            'name': 'Smartphone',
            'price': 699.99,
            'in_stock': True,
            'image': 'phone.jpg'
        },
        {
            'name': 'Laptop',
            'price': 1299.49,
            'in_stock': False,
            'image': 'laptop.jpg'
        },
        {
            'name': 'Headphones',
            'price': 199.95,
            'in_stock': True,
            'image': 'headphones.jpg'
        }
    ]
    return render_template('products.html', products=product_list)

if __name__ == '__main__':
    app.run(debug=True)
