import unittest
from math_quiz import random_number, random_operator, result


class TestMathGame(unittest.TestCase):

    def test_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        for _ in range(100):  # Run the test multiple times
            operator = random_operator()
            self.assertIn(operator, ['+', '-', '*'])
        pass

    def test_result(self):
            test_cases = [
                {'num1': 5, 'num2': 2, 'operator': '+', 'expected': ('5 + 2', 7)},
                {'num1': 8, 'num2': 3, 'operator': '-', 'expected': ('8 - 3', 5)},
                {'num1': 4, 'num2': 6, 'operator': '*', 'expected': ('4 * 6', 24)},
            ]

            for case in cases:
                with self.subTest(case=case):
                    problem, result_value = result(case['num1'], case['num2'], case['operator'])
                    self.assertEqual(problem, case['expected'][0])
                    self.assertEqual(result_value, case['expected'][1])

if __name__ == "__main__":
    unittest.main()
