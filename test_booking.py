import unittest
from booking import calculate_cost


class TestBooking(unittest.TestCase):

    def test_calculate_cost(self):
        self.assertEqual(calculate_cost(3, 200), 600)

    def test_invalid_hours(self):
        with self.assertRaises(ValueError):
            calculate_cost(0, 200)


if __name__ == "__main__":
    unittest.main()