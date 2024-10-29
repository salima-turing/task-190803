import unittest
from collections import defaultdict


class Aggregator:
    def __init__(self):
        self.data = defaultdict(list)

    def add_data(self, user_id, value):
        self.data[user_id].append(value)

    def aggregate_and_privatize(self):
        result = {}
        for user_id, values in self.data.items():
            # Simple aggregation: Sum up the values for privacy
            aggregated_value = sum(values)
            result[user_id] = aggregated_value
        return result


class TestAggregatePrivacy(unittest.TestCase):
    def test_privacy_protection(self):
        # Scenario: Verify that aggregated data is protected from individual values
        aggregator = Aggregator()
        user_id1 = "user1"
        user_id2 = "user2"

        aggregator.add_data(user_id1, 10)
        aggregator.add_data(user_id1, 20)
        aggregator.add_data(user_id2, 30)

        aggregated_data = aggregator.aggregate_and_privatize()

        self.assertEqual(aggregated_data[user_id1], 30, "Aggregated value for user1 is incorrect")
        self.assertEqual(aggregated_data[user_id2], 30, "Aggregated value for user2 is incorrect")

        # Individual values should not be exposed
        self.assertNotIn(10, aggregated_data.values(), "Individual value 10 leaked")
        self.assertNotIn(20, aggregated_data.values(), "Individual value 20 leaked")
        self.assertNotIn(30, [aggregated_data[user_id1]], "Individual value 30 leaked")


if __name__ == '__main__':
    unittest.main()
