import unittest

from age_input import get_age


class AgeInputTest(unittest.TestCase):
    def test_is_year_over_2022(self):
        self.assertEqual(0, get_age(2023))

    def test_is_over_18(self):
        self.assertEqual(get_age(1992), "over 18")


if __name__ == '__main__':
    unittest.main()
