from typing import List
from unittest import TestCase
from random import randint
from CORE_DataRepresentation.VernamCipher import VernamCipher


class Test(TestCase):

    def __test(self, key: List[int], test_cases: List[str]):
        my_cipher: VernamCipher = VernamCipher(key)
        for plain_text in test_cases:
            cipher_text: str = my_cipher.encrypt(plain_text)
            recovered_plain_text: str = my_cipher.decrypt(cipher_text)
            print("{} with key {} becomes {} then back to {}".format(
                plain_text,
                key,
                cipher_text,
                recovered_plain_text))
            self.assertEqual(plain_text.lower(), recovered_plain_text)

    def test_caesar(self):
        self.__test([5], ['hello'])
        self.__test([15], ['goodbye'])

    def test_one_time_pad(self):
        self.__test([randint(0, 20) for _ in range(20)], ["hello"])
