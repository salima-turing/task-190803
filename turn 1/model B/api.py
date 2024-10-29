# api.py
import flask
from flask import request, jsonify

app = flask.Flask(__name__)

# Sample data store (In a real application, this would be a database)
sample_data = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    # Add more sample data as needed
]

@app.route('/aggregate_data', methods=['GET'])
def aggregate_data():
    # Implement the aggregate privacy mechanism here
    aggregated_age = sum(data['age'] for data in sample_data)
    return jsonify({"aggregated_age": aggregated_age})

if __name__ == '__main__':
    app.run(debug=True)
