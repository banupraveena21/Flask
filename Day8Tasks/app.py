from flask import Flask, jsonify, request, make_response
import time
import random

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    {"id": 4, "name": "Diana", "email": "diana@example.com"},
    # Add more users if you want
]

products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
    {"id": 2, "name": "Phone", "price": 599.99, "in_stock": False},
    {"id": 3, "name": "Headphones", "price": 199.99, "in_stock": True},
    {"id": 4, "name": "Monitor", "price": 299.99, "in_stock": True},
    {"id": 5, "name": "Keyboard", "price": 49.99, "in_stock": False},
    # Add more products as needed
]

app_start_time = time.time()
app_version = "1.0.0"

@app.route('/api/time')
def get_time():
    # 1. Current server time as JSON
    return jsonify({"time": time.strftime("%Y-%m-%d %H:%M:%S")})

@app.route('/api/users')
def get_users():
    # 9. Pagination support: ?page=1&limit=2
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 2))
    except ValueError:
        page = 1
        limit = 2
    start = (page - 1) * limit
    end = start + limit
    paginated_users = users[start:end]
    return jsonify({
        "page": page,
        "limit": limit,
        "total": len(users),
        "users": paginated_users
    })

@app.route('/api/random')
def get_random():
    # 3. Return random number or message
    messages = ["Hello!", "Random Message", "Have a nice day!", "42", "Keep coding!"]
    choice = random.choice(messages + [str(random.randint(1, 100))])
    return jsonify({"random": choice})

@app.route('/api/status')
def get_status():
    uptime = int(time.time() - app_start_time)
    return jsonify({
        "status": "running",
        "uptime": uptime,
        "app_version": app_version
    })

@app.route('/api/products')
def get_products():
    # Return full products list, can add pagination similarly if needed
    return jsonify({"products": products})

@app.route('/api/greet')
def greet():
    # 7. Query param example: /api/greet?name=Arivu
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

# 8. Error handling with JSON
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# 10. Custom header example
@app.route('/api/custom-header')
def custom_header():
    data = {"message": "This response has a custom header"}
    response = make_response(jsonify(data))
    response.headers['X-Custom-Header'] = 'MyCustomHeaderValue'
    return response

if __name__ == '__main__':
    app.run(debug=True)
