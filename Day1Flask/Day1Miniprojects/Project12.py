# Simple Product Info Page
'''
Requirements:
• /product/<id> returns name, price, and stock status.
• Hardcode 3 products and fetch info based on ID.
• Add route /products that lists all product IDs and names in a table.
• Practice printing route access in terminal.
'''

from flask import Flask

app = Flask(__name__)

products = {
    "101": {"name": "Wireless Mouse", "price": "$25", "stock": True},
    "102": {"name": "Keyboard", "price": "$45", "stock": False},
    "103": {"name": "HD Monitor", "price": "$150", "stock": True}
}

@app.route("/product/<id>")
def product_detail(id):
    print(f"[INFO] /product/{id} accessed")
    
    product = products.get(id)
    if product:
        stock_status = "In Stock" if product["stock"] else "Out of Stock"
        return f"""
        <h2>Product Info</h2>
        <p><b>Name:</b> {product["name"]}</p>
        <p><b>Price:</b> {product["price"]}</p>
        <p><b>Status:</b> {stock_status}</p>
        """
    else:
        return f"<p style='color:red;'>Product with ID {id} not found.</p>"

@app.route("/products")
def list_products():
    print("[INFO] /products accessed")
    
    table_rows = ""
    for pid, info in products.items():
        table_rows += f"<tr><td>{pid}</td><td>{info['name']}</td></tr>"

    return f"""
    <h2>Product List</h2>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr><th>Product ID</th><th>Product Name</th></tr>
        {table_rows}
    </table>
    """

if __name__ == "__main__":
    app.run(debug=True)