from typing import List, Optional, Set
from unittest import TestCase

from CORE_DataRepresentation.VernamCipher import VernamCipher, generate_one_time_pad
from CORE_DataRepresentation.BreakVernamCipher import get_keys, get_words_set

WORDS_FILENAME: str = 'words_alpha.txt'


class Test(TestCase):

    def __test_encrypt_decrypt(self, key: List[int], test_cases: List[str]):
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
        self.__test_encrypt_decrypt([5], ['hello'])
        self.__test_encrypt_decrypt([15], ['goodbye'])

    def test_one_time_pad(self):
        self.__test_encrypt_decrypt(generate_one_time_pad(10), ["hello"])

    def test_word_set(self):
        words: Set[str] = get_words_set(WORDS_FILENAME)
        self.assertTrue('hello' in words)
        self.assertFalse('asdfasfafsdf' in words)

    def __test_break_vernam(self, key: List[int], test_cases: List[str]):
        for plain_text in test_cases:
            my_cipher: VernamCipher = VernamCipher(key)
            my_cipher_text: str = my_cipher.encrypt(plain_text)
            found_key, score = get_keys(my_cipher_text, len(key), WORDS_FILENAME)
            my_found_cipher: VernamCipher = VernamCipher(found_key)
            my_found_plain_text: str = my_found_cipher.decrypt(my_cipher_text)
            print('Brute force decrypt found {} and used it to decrypt\n{}\ninto\n{}'
                  .format(found_key, my_cipher_text, my_found_plain_text))
            self.assertEqual(1.0, score)
            self.assertEqual(plain_text.lower(), my_found_plain_text)

    def test_brute_force_caesar(self):
        self.__test_break_vernam([7],
                                 ['how now brown cow',
                                  'the rain in spain falls mainly on the plain'
                                  ])

    def test_brute_force_vernam(self):
        self.__test_break_vernam([3, 6],
                                 ['how now brown cow',
                                  'the rain in spain falls mainly on the plain'
                                  ])

    def test_brute_force_vernam_longer(self):
        self.__test_break_vernam(generate_one_time_pad(4),
                                 ['ive got a brand new combine harvester and I gave you the key',
                                  'the rain in spain falls mainly on the plain'
                                  ])
