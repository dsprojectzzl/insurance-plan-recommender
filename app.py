from flask import Flask, request, jsonify
from backend.logic import calculate_insurance_plan
from backend.database import get_all_plans_with_recommendation
from dotenv import load_dotenv
import os
import logging

load_dotenv()

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle user input and return the insurance plan UID.
    """
    try:
        user_data = request.json
        if not user_data:
            return jsonify({"error": "Invalid or missing input data"}), 400
        
        logger.info(f"Received user data: {user_data}")
        
        plan_uid = calculate_insurance_plan(user_data)
        
        logger.info(f"Recommended plan UID: {plan_uid}")
        
        return jsonify({"plan_uid": plan_uid}), 200
    except Exception as e:
        logger.error(f"Error in /predict: {e}", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/plans/<int:uid>', methods=['GET'])
def get_plan(uid):
    """
    Fetch all insurance plans and mark the recommended plan based on the UID.
    """
    try:
        # Fetch all plans
        plans = get_all_plans_with_recommendation(uid)
        
        # Check if at least one plan is recommended
        recommended_plans = [plan for plan in plans if plan.get("is_recommended")]
        if not recommended_plans:
            return jsonify({"error": "No plan found with the given UID"}), 404
        
        return jsonify(plans), 200
    except Exception as e:
        logger.error(f"Error in /plans/<uid>: {e}", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
