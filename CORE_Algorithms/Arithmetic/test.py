import unittest
from CORE_Algorithms.Arithmetic.ReversePolishNotation import ReversePolishNotation


class TestReversePolishNotation(unittest.TestCase):
    def test_simple(self):
        expression: ReversePolishNotation = ReversePolishNotation("AB+")

        ans1: float = expression.evaluate({'A': 4, 'B': 5})
        self.assertEqual(4 + 5, ans1)

        ans2: float = expression.evaluate({'A': 342, 'B': 53})
        self.assertEqual(342 + 53, ans2)
