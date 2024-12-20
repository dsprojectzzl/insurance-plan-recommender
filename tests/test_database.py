import unittest
from unittest.mock import patch
from backend.database import get_all_plans_with_recommendation

class TestDatabase(unittest.TestCase):
    @patch('backend.database.get_database_connection')
    def test_get_all_plans_with_recommendation_valid(self, mock_conn):
        mock_cursor = mock_conn.return_value.cursor.return_value
        mock_cursor.description = [
            ("UID",), ("Plan",), ("Premium",), ("Deductible",), ("Coverage",), ("AdditionalBenefits",)
        ]
        mock_cursor.fetchall.return_value = [
            (1, "Basic", "$100-$200", "$1000", "Limited coverage", "None"),
            (2, "Standard Plus", "$200-$400", "$500", "Comprehensive coverage", "Free gym membership"),
            (3, "Premium", "$400-$600", "$200", "Full coverage", "Priority support"),
        ]

        result = get_all_plans_with_recommendation(2)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

        for plan in result:
            if plan["UID"] == 2:
                self.assertTrue(plan["is_recommended"])
            else:
                self.assertFalse(plan["is_recommended"])

    @patch('backend.database.get_database_connection')
    def test_get_all_plans_with_recommendation_empty(self, mock_conn):
        mock_cursor = mock_conn.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = []

        result = get_all_plans_with_recommendation(2)

        self.assertIsInstance(result, dict)
        self.assertIn("error", result)
        self.assertEqual(result["error"], "No plans found")

if __name__ == '__main__':
    unittest.main()


