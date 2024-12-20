from flask import Flask, request, jsonify
from backend.logic import calculate_insurance_plan
from backend.database import get_plan_by_uid
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle user input and return the insurance plan UID.
    """
    try:
        user_data = request.json
        plan_uid = calculate_insurance_plan(user_data)
        return jsonify({"plan_uid": plan_uid})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/plans/<int:uid>', methods=['GET'])
def get_plan(uid):
    """
    Fetch insurance plan details by UID.
    """
    try:
        plan_details = get_plan_by_uid(uid)
        return jsonify(plan_details)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


