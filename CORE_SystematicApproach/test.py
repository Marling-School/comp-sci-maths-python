from unittest import TestCase
from CORE_SystematicApproach.factorial import factorial


class TestFactorial(TestCase):

    def test_simple(self):
        self.assertEqual(6, factorial(3))
        self.assertEqual(120, factorial(5))
        self.assertEqual(6, factorial(3))
        self.assertEqual(3628800, factorial(10))

    def test_negative(self):
        self.assertRaises(Exception, lambda _: factorial(-5))

    def test_wrong_type(self):
        self.assertRaises(Exception, lambda _: factorial('a'))
