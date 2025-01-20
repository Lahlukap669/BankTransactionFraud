from flask import Flask, jsonify, request, send_file, send_from_directory
import json
import hashlib
from flask_cors import CORS
import os
from joblib import dump, load
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
CORS(app) # Enable CORS

# load model
model = load(filename="./randomForestBankTransactionFraud.joblib")

## TESTING
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        podatki_json = request.get_json()
        
        # Extracting sent data
        V1 = podatki_json.get("V1")
        V2 = podatki_json.get("V2")
        V3 = podatki_json.get("V3")
        V4 = podatki_json.get("V4")
        V5 = podatki_json.get("V5")
        V6 = podatki_json.get("V6")
        V7 = podatki_json.get("V7")
        V8 = podatki_json.get("V8")
        V9 = podatki_json.get("V9")
        V10 = podatki_json.get("V10")
        V11 = podatki_json.get("V11")
        V12 = podatki_json.get("V12")
        V13 = podatki_json.get("V13")
        V14 = podatki_json.get("V14")
        V15 = podatki_json.get("V15")
        V16 = podatki_json.get("V16")
        V17 = podatki_json.get("V17")
        V18 = podatki_json.get("V18")
        V19 = podatki_json.get("V19")
        V20 = podatki_json.get("V20")
        V21 = podatki_json.get("V21")
        V22 = podatki_json.get("V22")
        V23 = podatki_json.get("V23")
        V24 = podatki_json.get("V24")
        V25 = podatki_json.get("V25")
        V26 = podatki_json.get("V26")
        V27 = podatki_json.get("V27")
        V28 = podatki_json.get("V28")
        Amount = podatki_json.get("Amount")

        # Load model
        columns = [f"V{i+1}" for i in range(29)]
        values = [
            V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount
        ]
        
        # Create the DataFrame
        data = pd.DataFrame([values], columns=columns)
        data.rename(columns={data.columns[-1]: 'Amount'}, inplace=True)
        predicted_probabilities = model.predict_proba(data)
        predicted_class = model.predict(data)[0]
        print(predicted_probabilities)
        if predicted_class == 0:
            return jsonify({'fraud': False,
                            'probability_of_normal-0': predicted_probabilities[0][0],
                            'probability_of_fraud-1': predicted_probabilities[0][1]})
        else:
            return jsonify({'fraud': True,
                            'probability_of_normal-0': predicted_probabilities[0][0],
                            'probability_of_fraud-1': predicted_probabilities[0][1]})
        
    return jsonify({'error': "GET method not allowed"}), 405

if __name__ == "__main__":
    app.run(debug=True, host='', port=5000)