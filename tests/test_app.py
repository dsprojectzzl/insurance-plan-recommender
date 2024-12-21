import unittest
from app import app
import json

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        """
        Test the /predict endpoint.
        """
        input_data = {
            "Heart_Rate_BPM": 85,
            "Sleep_Duration_Hours": 7.5,
            "Physical_Activity_Steps": 12000,
            "Mood_Rating": 8
        }

        print("\n=== Test /predict Endpoint ===")
        print("Input Data:", json.dumps(input_data, indent=4))

        # Send request
        response = self.app.post('/predict', data=json.dumps(input_data), content_type='application/json')
        print("Response Status Code:", response.status_code)

        # Verify response
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        print("Response Data:", json.dumps(response_data, indent=4))

        # Validate response structure
        self.assertIn("plan_uid", response_data)
        self.assertIsInstance(response_data["plan_uid"], int)

    def test_get_plan_endpoint(self):
        """
        Test the /plans/<uid> endpoint.
        """
        print("\n=== Test /plans/<uid> Endpoint ===")
        
        # Test with a valid UID
        valid_uid = 2
        print(f"Fetching plans with recommended UID: {valid_uid}")
        response = self.app.get(f'/plans/{valid_uid}')
        print("Response Status Code:", response.status_code)

        # Verify response
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        print("Response Data:", json.dumps(response_data, indent=4))

        # Validate response structure
        self.assertIsInstance(response_data, list)
        recommended_plans = [plan for plan in response_data if plan["is_recommended"]]
        self.assertEqual(len(recommended_plans), 1)
        self.assertEqual(recommended_plans[0]["UID"], valid_uid)

        # Test with an invalid UID
        invalid_uid = 9999
        print(f"Fetching plans with invalid UID: {invalid_uid}")
        response = self.app.get(f'/plans/{invalid_uid}')
        print("Response Status Code:", response.status_code)

        # Verify response
        self.assertEqual(response.status_code, 404)
        response_data = response.get_json()
        print("Response Data:", json.dumps(response_data, indent=4))

        # Validate error message
        self.assertIn("error", response_data)
        self.assertEqual(response_data["error"], "No plan found with the given UID")

if __name__ == '__main__':
    unittest.main()
