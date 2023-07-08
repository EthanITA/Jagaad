import unittest

from .message import Message


class TestMessageModel(unittest.TestCase):

    def test_from_json_valid(self):
        test_json = {
            "uuid": "testuuid",
            "customerId": 1,
            "type": "test",
            "amount": "1.123"
        }

        message = Message.from_json(test_json)
        self.assertEqual(message.uuid, "testuuid")
        self.assertEqual(message.customerId, 1)
        self.assertEqual(message.type, "test")
        self.assertEqual(message.amount, "1.123")

    def test_from_json_invalid(self):
        test_json = {
            "uuid": "testuuid",
            "customerId": 1,
            "type": "test",
            "amount": "1.1234"
        }

        message = Message.from_json(test_json)
        self.assertIsNone(message)

    def test_get_customer_stats(self):
        messages = [
            Message("uuid1", 1, "A", "1.000"),
            Message("uuid2", 1, "A", "2.000"),
            Message("uuid3", 1, "B", "3.000"),
            Message("uuid4", 2, "A", "4.000"),
        ]

        stats = Message.get_customer_stats(1, messages)
        self.assertEqual(len(stats), 2)

        stats.sort(key=lambda x: x['type'])

        self.assertEqual(stats[0]['type'], "A")
        self.assertEqual(stats[0]['count'], 2)
        self.assertEqual(stats[0]['totalAmount'], 3.000)

        self.assertEqual(stats[1]['type'], "B")
        self.assertEqual(stats[1]['count'], 1)
        self.assertEqual(stats[1]['totalAmount'], 3.000)


if __name__ == "__main__":
    unittest.main()
