from flask import Flask, request, jsonify, render_template
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route for rendering the homepage
@app.route('/')
def index():
    return render_template('index.html')  # Home page

# Route for structured access like /Student/Index_json with filters
@app.route("/Student/Index_json", methods=["GET"])
def student_index():
    city = request.args.get('City')  # Retrieve 'City' query parameter
    gender = request.args.get('Gender')  # Retrieve 'Gender' query parameter
    
    with open('students.json') as f:
        data = json.load(f)  # Load students data from JSON

    # Apply filters based on City and Gender parameters
    if city and gender:
        filtered_data = [x for x in data if x['City'].lower() == city.lower() and x['Gender'].lower() == gender.lower()]
    elif city:
        filtered_data = [x for x in data if x['City'].lower() == city.lower()]
    elif gender:
        filtered_data = [x for x in data if x['Gender'].lower() == gender.lower()]
    else:
        filtered_data = data  # If no filters are applied, return all data

    return jsonify(filtered_data), 200

if __name__ == "__main__":
    app.run(debug=True)
