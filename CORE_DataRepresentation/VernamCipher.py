from typing import List


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
            if 'a' <= p <= 'z':
                c_ord: int = (ord(p) + (direction * key_this_char))
                if c_ord > ord('z'):
                    c_ord -= 26
                if c_ord < ord('a'):
                    c_ord += 26
                c: str = chr(c_ord)
                output_chars.append(c)
                # print("Processing {} in dir {} with key [{}] {} to make {}-{}".format(
                #     p, direction, key_index, key_this_char, c_ord, c))
            else:
                output_chars.append(p)
            key_index = (key_index + 1) % len(self.__one_time_pad)

        return "".join(output_chars)

    def encrypt(self, plain_text: str) -> str:
        return self.__process(plain_text, 1)

    def decrypt(self, cipher_text: str) -> str:
        return self.__process(cipher_text, -1)
