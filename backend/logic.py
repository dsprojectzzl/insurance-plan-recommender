import pickle
import numpy as np
import pandas as pd

model_path = 'models/trained_model.pkl'

with open(model_path, 'rb') as file:
    model = pickle.load(file)

import pandas as pd

def calculate_insurance_plan(user_data):
    """
    Use the trained model to calculate a score and determine the insurance plan UID.
    """
    features = pd.DataFrame([user_data])
    probabilities = model.predict_proba(features)

    score = probabilities[0][1]

    if score > 0.8:
        plan_uid = 1  # UID for "Enhanced Plan"
    elif score > 0.5:
        plan_uid = 2  # UID for "Standard Plus Plan"
    else:
        plan_uid = 3  # UID for "Standard Plan"

    return plan_uid
