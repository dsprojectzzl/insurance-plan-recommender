import unittest
from backend.logic import calculate_insurance_plan

class TestLogic(unittest.TestCase):
    def test_calculate_insurance_plan(self):
        """
        Test calculate_insurance_plan with sample user data.
        """
        user_data = {
            "Heart_Rate_BPM": 85,
            "Sleep_Duration_Hours": 7.5,
            "Physical_Activity_Steps": 12000,
            "Mood_Rating": 8
        }

        result = calculate_insurance_plan(user_data)

        self.assertIn(result, [1, 2, 3])

    def test_calculate_insurance_plan_edge_cases(self):
        """
        Test calculate_insurance_plan with edge cases.
        """
        # Very low scores
        user_data_low = {
            "Heart_Rate_BPM": 120,
            "Sleep_Duration_Hours": 2,
            "Physical_Activity_Steps": 0,
            "Mood_Rating": 1
        }
        self.assertEqual(calculate_insurance_plan(user_data_low), 2)

        # Very high scores
        user_data_high = {
            "Heart_Rate_BPM": 60,
            "Sleep_Duration_Hours": 10,
            "Physical_Activity_Steps": 20000,
            "Mood_Rating": 10
        }
        self.assertEqual(calculate_insurance_plan(user_data_high), 3)
if __name__ == '__main__':
    unittest.main()
