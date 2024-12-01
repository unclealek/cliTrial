import pandas as pd
from flask import Flask, jsonify, request
import os
import logging

# Initialize Flask app and logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def load_data():
    file_path = 'Clinical trials.xlsx'
    if not os.path.exists(file_path):
        logging.error(f"File not found at {file_path}")
        return None
    try:
        data = pd.read_excel(
            file_path,
            usecols=['Website', 'Company', 'Description'],
            engine='openpyxl'
        )
        logging.info(f"Data loaded successfully with shape: {data.shape}")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {str(e)}")
        return None

# Load data at app startup
app.config['DATA'] = load_data()

@app.route('/api/data', methods=['GET'])
def get_all_data():
    data = app.config['DATA']
    if data is None:
        return jsonify({
            "error": "Data not available",
            "message": "Could not load the Excel file. Please check the file path and format."
        }), 500
    try:
        data_dict = data.to_dict(orient='records')
        return jsonify({
            "status": "success",
            "total_records": len(data_dict),
            "data": data_dict
        })
    except Exception as e:
        logging.error(f"Error processing data: {str(e)}")
        return jsonify({
            "error": "Error processing data",
            "message": str(e)
        }), 500

@app.route('/api/companies/search', methods=['GET'])
def search_companies_by_letter():
    data = app.config['DATA']
    if data is None:
        return jsonify({"error": "Data not available"}), 500

    letter = request.args.get('letter', '').strip().upper()
    if len(letter) != 1 or not letter.isalpha():
        return jsonify({"error": "Please provide a single letter parameter"}), 400

    filtered_companies = data[data['Company'].str.upper().str.startswith(letter)]
    return jsonify({
        "letter": letter,
        "total_records": len(filtered_companies),
        "companies": filtered_companies.to_dict(orient='records')
    })

@app.route('/api/companies/stats', methods=['GET'])
def get_company_stats():
    data = app.config['DATA']
    if data is None:
        return jsonify({"error": "Data not available"}), 500

    company_counts = data['Company'].str[0].str.upper().value_counts().to_dict()
    return jsonify({
        "statistics": {
            "companies_by_letter": company_counts,
            "total_companies": len(data)
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
