from unittest import TestCase
from typing import Optional, List, Tuple
from CORE_TheoryOfComputation.BackusNaurForm.BackusNaurForm import BackusNaurForm


class TestBNF(TestCase):

    def test_digit(self):
        bnf: BackusNaurForm = BackusNaurForm()\
            .add_rule("<digit> ::= 0|1|2|3|4|5|6|7|8|9")
        print("Test Digit: {}".format(bnf))

        test_cases: List[Tuple[str, Optional[str]]] = [
            ('6', 'digit'),
            ('458', None),
            ('X', None),
            ('JOE', None)
        ]

        for test_input, expected_output in test_cases:
            actual_output: Optional[str] = bnf.find_match(test_input)
            self.assertEqual(expected_output, actual_output)

    def test_integer(self):
        bnf: BackusNaurForm = BackusNaurForm()\
            .add_rule("<digit> ::= 0|1|2|3|4|5|6|7|8|9")\
            .add_rule("<integer> ::= <digit> | <digit><integer>")
        print("Test Integer: {}".format(bnf))

        test_cases: List[Tuple[str, Optional[str]]] = [
            ('6', 'digit'),
            ('458', 'integer'),
            ('X', None),
            ('JOE', None)
        ]

        for test_input, expected_output in test_cases:
            actual_output: Optional[str] = bnf.find_match(test_input)
            self.assertEqual(expected_output, actual_output)

    def test_real(self):
        bnf: BackusNaurForm = BackusNaurForm()\
            .add_rule("<digit> ::= 0|1|2|3|4|5|6|7|8|9")\
            .add_rule("<integer> ::= <digit> | <digit><integer>")\
            .add_rule("<real> ::= <integer> | <integer>'.'<integer>")
        print("Test Real: {}".format(bnf))

        test_cases: List[Tuple[str, Optional[str]]] = [
            ('6', 'digit'),
            ('457', 'integer'),
            ('3.567', 'real'),
            ('X', None),
            ('JOE', None)
        ]

        for test_input, expected_output in test_cases:
            actual_output: Optional[str] = bnf.find_match(test_input)
            self.assertEqual(expected_output, actual_output)

    def test_expression(self):
        bnf: BackusNaurForm = BackusNaurForm()\
            .add_rule("<digit> ::= 0|1|2|3|4|5|6|7|8|9") \
            .add_rule("<integer> ::= <digit> | <digit><integer>")\
            .add_rule("<compare>::= < | > | <= | >= | == | !=")\
            .add_rule("<bool>::= <integer> <compare> <integer>")
        print("Test Expression: {}".format(bnf))

        test_cases: List[Tuple[str, Optional[str]]] = [
            ('<', 'compare'),
            ('4 < 5', 'bool'),
            ('X', None),
            ('JOE', None)
        ]

        for test_input, expected_output in test_cases:
            actual_output: Optional[str] = bnf.find_match(test_input)
            self.assertEqual(expected_output, actual_output)