from typing import List
from enum import Enum
from random import randint

"""
the list of characters that we can encrypt. Any encryption will find the index
in this list, then rotate that index forward by the key and read off the output char.
"""
ALPHABET: List[str] = [chr(x) for x in range(ord('a'), ord('z'))]


def generate_one_time_pad(length: int) -> List[int]:
    """
    Utility function for generating a new random one time pad.
    :param length: The length of the OTP to generate
    :return: A list of values that make up the OTP
    """
    return [randint(0, len(ALPHABET)) for _ in range(length)]


class Direction(Enum):
    """
    Used internally to indicate which direction we are processing a message.
    """
    DECRYPT = -1
    ENCRYPT = 1


class VernamCipher:
    """
    Encapsulates the vernam cipher. It can be used to run Caesar cipher if the key is
    of length 1.
    """
    # The encryption key
    __one_time_pad: List[int]

    def __init__(self, one_time_pad: List[int]):
        """
        Construct a new Vernam Cipher processor object for a given key.
        :param one_time_pad: The OTP to use, must be at least one item.
        """
        if len(one_time_pad) == 0:
            raise Exception("The encryption key must contain at least one value")
        self.__one_time_pad = one_time_pad

    def __process(self, message: str, direction: Direction) -> str:
        """
        Given a message, it calculates a shifted version. The direction means
        that this function can be used for decryption (-1) and encryption (+1).
        :param message: The message to encrypt or decrypt
        :param direction: Indicates if we are decrypting or encrypting
        :return:
        """
        # Keep track of the output chars
        output_chars: List[str] = []

        # Iterate through the key, rotate to the start when we reach its end
        key_index = 0

        # Convert message to lowercase, then iterate through each character
        for p in message.lower():
            # Lookup the key
            key_this_char: int = self.__one_time_pad[key_index]
            try:
                # Find the index of the given character
                index: int = ALPHABET.index(p)

                # Move it on by the key, and make sure we rotate around the end and start
                index += len(ALPHABET)
                index += (direction.value * key_this_char)
                index %= len(ALPHABET)

                # Write the ALPHABET character at the shifted index to the output
                output_chars.append(ALPHABET[index])

            except ValueError:
                # If the character is not in the alphabet, just shove it as-is into the output
                output_chars.append(p)

            key_index = (key_index + 1) % len(self.__one_time_pad)

        # Build the output string from the chars
        return "".join(output_chars)

    def encrypt(self, plain_text: str) -> str:
        """
        Encrypt some plain text with the key that belongs to this instance of the cipher
        :param plain_text: The plain text to encrypt
        :return: The cipher text
        """
        return self.__process(plain_text, Direction.ENCRYPT)

    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypt some cipher text with the key that belongs to this instance of the cipher
        :param cipher_text: The cipher text to decrypt
        :return: The plain text
        """
        return self.__process(cipher_text, Direction.DECRYPT)
