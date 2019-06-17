import unittest
from typing import List
from CORE_TheoryOfComputation.generate_permutations import generate_permutations


class Test(unittest.TestCase):

    def test_generate_inputs(self):
        my_inputs: List[str] = []
        generate_permutations({"0", "1"}, lambda x: my_inputs.append(x), 3)
        print("Inputs Generated: {}".format(my_inputs))
