from typing import List
from unittest import TestCase

from CORE_DataRepresentation.VernamCaesarCipher.VernamCipher import VernamCipher, generate_one_time_pad
from CORE_DataRepresentation.VernamCaesarCipher.BreakVernamCipher import get_keys

WORDS_FILENAME: str = 'words_alpha.txt'


class Test(TestCase):

    def __test_encrypt_decrypt(self, key: List[int], test_cases: List[str]):
        """
        General form of tests that encrypt and decrypt some data.
        This test checks that the decryption successfully recovers the data.
        :param key: The key to use
        :param test_cases: A list of strings to encrypt and decrypt
        """

        # Create a cipher with this key
        my_cipher: VernamCipher = VernamCipher(key)
        for plain_text in test_cases:

            # Call upon the cipher to encrypt then decrypt that plain text
            cipher_text: str = my_cipher.encrypt(plain_text)
            recovered_plain_text: str = my_cipher.decrypt(cipher_text)

            # Does the recovered plain text match the given plain text?
            self.assertEqual(plain_text.lower(), recovered_plain_text)

    def test_caesar(self):
        self.__test_encrypt_decrypt([5], ["hello"])
        self.__test_encrypt_decrypt([15], ["there once was a fellow called hank"])

    def test_one_time_pad(self):
        self.__test_encrypt_decrypt(generate_one_time_pad(10),
                                    ["hello", "it was the best of times, it was the worst of times"])

    def __test_break_vernam(self, key: List[int], test_cases: List[str]):
        """
        General form of a brute force attack test.
        :param key: The key to use
        :param test_cases: Strings to encrypt and then attempt decrypt
        """
        # Create a cipher for this key
        my_cipher: VernamCipher = VernamCipher(key)

        for plain_text in test_cases:
            # Call upon the cipher to encrypt our string
            my_cipher_text: str = my_cipher.encrypt(plain_text)

            # Attempt to find a key
            found_key, score = get_keys(my_cipher_text, len(key), WORDS_FILENAME)

            # Try to decrypt with that found key
            my_found_cipher: VernamCipher = VernamCipher(found_key)
            my_found_plain_text: str = my_found_cipher.decrypt(my_cipher_text)

            # Does the found plain text match the give plain text?
            self.assertEqual(plain_text.lower(), my_found_plain_text)

    def test_brute_force_caesar(self):
        self.__test_break_vernam([7],
                                 ['how now brown cow',
                                  'the rain in spain falls mainly on the plain'
                                  ])

    def test_brute_force_vernam(self):
        self.__test_break_vernam([3, 6],
                                 ['there once was a fellow called Fred',
                                  'the rain in spain falls mainly on the plain'
                                  ])

    def test_brute_force_vernam_longer(self):
        self.__test_break_vernam(generate_one_time_pad(4),
                                 ['ive got a brand new combine harvester and I gave you the key',
                                  'the rain in spain falls mainly on the plain'
                                  ])
