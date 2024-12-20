import unittest
from unittest.mock import patch
from backend.database import get_plan_by_uid

class TestDatabase(unittest.TestCase):
    @patch('backend.database.get_database_connection')
    def test_get_plan_by_uid_valid(self, mock_conn):
        mock_cursor = mock_conn.return_value.cursor.return_value
        mock_cursor.description = [("UID",), ("Plan",), ("Premium",), ("Deductible",), ("Coverage",), ("AdditionalBenefits",)]
        mock_cursor.fetchone.return_value = (1, "Standard Plus", "$200-$400", "$500", "Comprehensive coverage", "Free gym membership")

        result = get_plan_by_uid(1)
        self.assertIsNotNone(result)
        self.assertIn("Plan", result)
        self.assertEqual(result["UID"], 1)

    @patch('backend.database.get_database_connection')
    def test_get_plan_by_uid_invalid(self, mock_conn):
        mock_cursor = mock_conn.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = None

        result = get_plan_by_uid(9999)
        self.assertIsNotNone(result)
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Plan not found")

if __name__ == '__main__':
    unittest.main()

