# test_api.py
import unittest
import requests
import json
from api import sample_data


class TestAggregatePrivacy(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000'  # Ensure this matches the API server's URL

    def test_aggregate_data_privacy(self):
        # Test 1: Verify if the aggregated age is correct
        response = requests.get(self.base_url + '/aggregate_data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['aggregated_age'],
                         55)  # Ensure this matches the expected aggregated age based on the sample data

        # Test 2: Check if the aggregated age is not exposed in the individual data items
        for data_item in sample_data:
            with self.subTest(data_item=data_item):
                self.assertNotIn('aggregated_age', data_item,
                                 msg="Aggregated age should not be exposed in individual data items.")


if __name__ == '__main__':
    unittest.main()
