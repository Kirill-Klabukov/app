from flask import Flask, request, jsonify, render_template
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route for rendering the homepage
@app.route('/')
def index():
    return render_template('index.html')  # This will render a simple HTML page

# Route for filtering students
@app.route("/Students", methods=["GET"])
def main():
    city = request.args.get('City')  # Retrieve 'City' query parameter
    with open('students.json') as f:
        data = json.load(f)  # Load students data from JSON

    if city:
        # Filter data based on the 'City' parameter
        filtered_data = [x for x in data if x['City'].lower() == city.lower()]
        return jsonify(filtered_data), 200
    else:
        return jsonify(data), 200  # If no city parameter, return all data

if __name__ == "__main__":
    app.run(debug=True)
