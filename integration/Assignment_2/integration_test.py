# Integration tests
import unittest

# Define the function to be tested
def categorize_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

class TestCategorizeNumber(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(categorize_number(5), "positive")

    def test_negative(self):
        self.assertEqual(categorize_number(-3), "negative")

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
