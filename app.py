from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for all routes (can be configured more specifically in production)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Environment variable for counter file path (adjust this based on your deployment environment)
COUNTER_FILE = os.getenv("COUNTER_FILE", "counter.txt")

# Ensure counter file exists
def initialize_counter():
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as file:
            file.write("0")

# Read the current counter value
def get_counter():
    with open(COUNTER_FILE, "r") as file:
        return int(file.read().strip())

# Increment and save the counter value
def increment_counter():
    new_count = get_counter() + 1
    with open(COUNTER_FILE, "w") as file:
        file.write(str(new_count))
    return new_count

@app.route('/api/get_count', methods=['GET'])
def get_count():
    count = get_counter()
    return jsonify({"count": count})

@app.route('/api/increment_count', methods=['POST'])
def increment_count():
    new_count = increment_counter()
    return jsonify({"count": new_count})

if __name__ == '__main__':
    # Initialize counter file
    initialize_counter()

    # For production, app.run() should not be used. Instead, use a WSGI server like Gunicorn.
    # The app.run() method should only be used for local testing.
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
