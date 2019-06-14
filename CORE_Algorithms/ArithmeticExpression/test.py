import unittest
from CORE_Algorithms.ArithmeticExpression.ArithmeticExpression import ArithmeticExpression
from CORE_Algorithms.ReversePolishNotation.ReversePolishNotation import ReversePolishNotation


class TestArithmeticExpression(unittest.TestCase):
    def test(self):
        my_expression: ArithmeticExpression = ArithmeticExpression("((A+B)*(C+D))")
        print("My Expression: {}".format(my_expression))

    def test_complex_1(self):
        my_expression: ArithmeticExpression = ArithmeticExpression("((A + B) * (C - D))")
        print("My Expression: {}".format(my_expression))
        rpn: ReversePolishNotation = ReversePolishNotation(my_expression.postfix())

        ans1: float = rpn.evaluate({"A": 9, "B": 2, "C": 15, "D": 7})
        self.assertEqual((9 + 2) * (15 - 7), ans1)

        ans2: float = rpn.evaluate({"A": 91, "B": 12, "C": 7, "D": 45})
        self.assertEqual((91 + 12) * (7 - 45), ans2)

    def test_complex_2(self):
        my_expression: ArithmeticExpression = ArithmeticExpression("((B/(C+D))*A)")
        print("My Expression: {}".format(my_expression))
        rpn: ReversePolishNotation = ReversePolishNotation(my_expression.postfix())

        ans1: float = rpn.evaluate({"A": 45, "B": 3, "C": 6, "D": 17})
        self.assertEqual((3 / (6 + 17)) * 45, ans1)

        ans2: float = rpn.evaluate({"A": 13, "B": 4, "C": 61, "D": 2})
        self.assertEqual((4 / (61 + 2)) * 13, ans2)
