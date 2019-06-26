from typing import List
from random import randint

ALPHABET: List[str] = [chr(x) for x in range(ord('a'), ord('z'))]


def generate_one_time_pad(length: int) -> List[int]:
    return [randint(0, len(ALPHABET)) for _ in range(length)]


class VernamCipher:
    """
    Encapsulates the vernam cipher. It can be used to run Caesar cipher if the key is
    of length 1.
    """
    # The encryption key
    __one_time_pad: List[int]

    def __init__(self, one_time_pad: List[int]):
        if len(one_time_pad) == 0:
            raise Exception("The encryption key must contain at least one value")
        self.__one_time_pad = one_time_pad

    def __process(self, message: str, direction: int) -> str:
        output_chars: List[str] = []
        key_index = 0

        for p in message.lower():
            key_this_char: int = self.__one_time_pad[key_index] % 26
            try:
                index: int = ALPHABET.index(p)
                index += len(ALPHABET)
                index += (direction * key_this_char)
                index %= len(ALPHABET)
                output_chars.append(ALPHABET[index])

            except ValueError:
                output_chars.append(p)

            key_index = (key_index + 1) % len(self.__one_time_pad)

        return "".join(output_chars)

    def encrypt(self, plain_text: str) -> str:
        return self.__process(plain_text, 1)

    def decrypt(self, cipher_text: str) -> str:
        return self.__process(cipher_text, -1)
