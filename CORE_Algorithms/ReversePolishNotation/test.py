import unittest
from CORE_Algorithms.ReversePolishNotation.ReversePolishNotation import ReversePolishNotation


class TestReversePolishNotation(unittest.TestCase):
    def test_sum(self):
        expression: ReversePolishNotation = ReversePolishNotation("AB+")

        ans1: float = expression.evaluate({"A": 4, "B": 5})
        self.assertEqual(4 + 5, ans1)

        ans2: float = expression.evaluate({"A": 342, "B": 53})
        self.assertEqual(342 + 53, ans2)

    def test_subtract(self):
        expression: ReversePolishNotation = ReversePolishNotation("AB-")

        ans1: float = expression.evaluate({"A": 4, "B": 5})
        self.assertEqual(4 - 5, ans1)

        ans2: float = expression.evaluate({"A": 342, "B": 53})
        self.assertEqual(342 - 53, ans2)

    def test_divide(self):
        expression: ReversePolishNotation = ReversePolishNotation("AB/")

        ans1: float = expression.evaluate({"A": 4, "B": 5})
        self.assertEqual(4 / 5, ans1)

        ans2: float = expression.evaluate({"A": 342, "B": 53})
        self.assertEqual(342 / 53, ans2)

    def test_multiply(self):
        expression: ReversePolishNotation = ReversePolishNotation("AB*")

        ans1: float = expression.evaluate({"A": 4, "B": 5})
        self.assertEqual(4 * 5, ans1)

        ans2: float = expression.evaluate({"A": 342, "B": 53})
        self.assertEqual(342 * 53, ans2)

    def test_complex_1(self):
        expression: ReversePolishNotation = ReversePolishNotation("AB+CD-*")

        ans1: float = expression.evaluate({"A": 9, "B": 2, "C": 15, "D": 7})
        self.assertEqual((9 + 2) * (15 - 7), ans1)

        ans2: float = expression.evaluate({"A": 91, "B": 12, "C": 7, "D": 45})
        self.assertEqual((91 + 12) * (7 - 45), ans2)

    def test_complex_2(self):
        expression: ReversePolishNotation = ReversePolishNotation("ABCD+/*")

        ans1: float = expression.evaluate({"A": 45, "B": 3, "C": 6, "D": 17})
        self.assertEqual((3 / (6 + 17)) * 45, ans1)

        ans2: float = expression.evaluate({"A": 13, "B": 4, "C": 61, "D": 2})
        self.assertEqual((4 / (61 + 2)) * 13, ans2)
