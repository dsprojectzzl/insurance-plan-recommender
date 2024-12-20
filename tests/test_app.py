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

        response = self.app.post('/predict', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response_data = response.get_json()
        self.assertIn("plan_uid", response_data)
        self.assertIsInstance(response_data["plan_uid"], int)

    def test_get_plan_endpoint(self):
        """
        Test the /plans/<uid> endpoint.
        """
        response = self.app.get('/plans/2')
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()

        self.assertIsInstance(response_data, list)

        recommended_plans = [plan for plan in response_data if plan["is_recommended"]]
        self.assertEqual(len(recommended_plans), 1)
        self.assertEqual(recommended_plans[0]["UID"], 2)

        response = self.app.get('/plans/9999')
        self.assertEqual(response.status_code, 404)
        response_data = response.get_json()
        self.assertIn("error", response_data)
        self.assertEqual(response_data["error"], "No plan found with the given UID")

if __name__ == '__main__':
    unittest.main()
