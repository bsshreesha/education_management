from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

# Initialize Flask app
app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB URI
db = client['education_db']
collection = db['education_details']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        data = request.json

        # Concatenate fields as required
        record = {
            "student_name": f"{data['student_prefix']} {data['student_name'].upper()}",
            "father_name": f"{data['father_prefix']} {data['father_name'].upper()}",
            "mother_name": f"{data['mother_prefix']} {data['mother_name'].upper()}",
            "student_mobile": f"{data['student_mobile']}",
            "father_mobile": f"{data['father_mobile']}",
            "mother_mobile": f"{data['mother_mobile']}",
            "school_name": data['school_name'],
            "standard": data['standard'],
            "start_year": data['start_year'],
            "end_year": data['end_year'],
            "year_of_passing": data['year_of_passing'],
            "board": data['board'],
            "total_years": data['total_years'],
            "email": data['email'],
            "date_of_birth": data['date_of_birth'],
        }

        # Insert into MongoDB
        result = collection.insert_one(record)
        record['_id'] = str(result.inserted_id)
        return jsonify(record), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    try:
        records = list(collection.find())
        for record in records:
            record['_id'] = str(record['_id'])
        return jsonify(records), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
