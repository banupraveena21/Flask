# 9. Product Warranty Checker
'''
Requirements:
- /check-warranty: Form with product serial (POST)
- /result?serial=ABC123 shows query-based response
- /warranty/<product> returns warranty for specific product using dynamic routing
- Redirect to confirmation page after checking
'''

from flask import Flask, request, redirect, url_for

app = Flask(__name__)


warranty_db = {
    'ABC123': {'product': 'Laptop X1', 'status': 'Valid until 2026-01-01'},
    'XYZ789': {'product': 'Smartphone Z5', 'status': 'Expired on 2024-06-15'},
    'LMN456': {'product': 'Tablet A2', 'status': 'Valid until 2025-12-31'}
}

product_warranties = {
    'laptop': '2 years from date of purchase',
    'smartphone': '1 year from date of purchase',
    'tablet': '18 months from date of purchase'
}


@app.route('/check-warranty', methods=['GET', 'POST'])
def check_warranty():
    if request.method == 'POST':
        serial = request.form.get('serial', '').strip().upper()
        return redirect(url_for('warranty_result', serial=serial))
    
    return '''
    <h2>Warranty Checker</h2>
    <form method="POST">
        Enter Product Serial Number: <br>
        <input type="text" name="serial" required><br><br>
        <input type="submit" value="Check Warranty">
    </form>
    '''


@app.route('/result')
def warranty_result():
    serial = request.args.get('serial', '').upper()
    info = warranty_db.get(serial)
    
    if not info:
        return f"<p>No warranty information found for serial: <strong>{serial}</strong></p>"

    return f'''
    <h3>Warranty Information</h3>
    <p><strong>Product:</strong> {info["product"]}</p>
    <p><strong>Status:</strong> {info["status"]}</p>
    '''


@app.route('/warranty/<product>')
def product_warranty(product):
    product = product.lower()
    warranty_info = product_warranties.get(product)
    
    if not warranty_info:
        return f"<h3>No warranty policy found for '{product}'</h3>", 404

    return f"<h3>{product.title()} Warranty Policy</h3><p>{warranty_info}</p>"


if __name__ == '__main__':
    app.run(debug=True)