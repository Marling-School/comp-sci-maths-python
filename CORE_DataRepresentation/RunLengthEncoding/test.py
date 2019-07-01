from unittest import TestCase
from typing import List
from CORE_DataRepresentation.RunLengthEncoding.run_length_encode import \
    run_length_encode, run_length_decode


class TestRLE(TestCase):

    def test_str(self):
        input_str: str = 'xxxxxxyyyyyzzzzzxxxxx'
        encoded = run_length_encode(input_str)
        decoded = run_length_decode(encoded)
        decoded_str = "".join(decoded)
        print("Encoded: {}".format(encoded))
        print("Decoded: {}".format(decoded))
        self.assertEqual(input_str, decoded_str)

    def test_num(self):
        input_str: List[int] = [4, 4, 4, 4, 4, 4, 5, 5, 5, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1]
        encoded = run_length_encode(input_str)
        decoded = run_length_decode(encoded)
        print("Encoded: {}".format(encoded))
        print("Decoded: {}".format(decoded))
        self.assertEqual(input_str, decoded)
