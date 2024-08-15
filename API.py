from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Path to store the counter in a text file
counter_file = "counter.txt"

# Function to read the counter from the file
def get_counter():
    if os.path.exists(counter_file):
        with open(counter_file, "r") as file:
            return int(file.read().strip())
    return 0

# Function to increment and save the counter to the file
def increment_counter():
    current_count = get_counter() + 1
    with open(counter_file, "w") as file:
        file.write(str(current_count))
    return current_count

@app.route('/api/get_count', methods=['GET'])
def get_count():
    # Return the current view count
    count = get_counter()
    return jsonify({"count": count})

@app.route('/api/increment_count', methods=['POST'])
def increment_count():
    # Increment the view count and return the updated value
    new_count = increment_counter()
    return jsonify({"count": new_count})

if __name__ == '__main__':
    # Create the counter file if it doesn't exist
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as file:
            file.write("0")
    app.run(debug=True)
