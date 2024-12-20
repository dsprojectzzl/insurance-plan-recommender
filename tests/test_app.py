import unittest
from app import app
import json

class TestApp(unittest.TestCase):
    def setUp(self):
        """
        Set up a test client for the Flask app.
        """
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
        response = self.app.get('/plans/1')
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIn("Plan", response_data)

        response = self.app.get('/plans/9999')
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIn("error", response_data)

if __name__ == '__main__':
    unittest.main()
