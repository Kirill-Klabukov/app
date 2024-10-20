
from flask import Flask
from flask import request
from flask import jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/Students", methods=["GET"])
def main():
    city = request.args.get('City')  # Retrieve 'City' query parameter
    f = open('students.json')
    data = json.load(f)  # Load students data from JSON
    f.close()

    if city:
        # Filter data based on the 'City' parameter
        filtered_data = [x for x in data if x['City'].lower() == city.lower()]
        return jsonify(filtered_data), 200
    else:
        return jsonify(data), 200  # If no city parameter, return all data

if __name__ == "__main__":
    app.run()
