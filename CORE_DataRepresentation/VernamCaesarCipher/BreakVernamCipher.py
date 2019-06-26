"""
I took a list of english words from this:
https://github.com/dwyl/english-words/blob/master/words_alpha.txt
"""
from typing import List, Set, Optional, Callable, Tuple
from CORE_DataRepresentation.VernamCaesarCipher.VernamCipher import VernamCipher, ALPHABET


def generate_keys(callback: Callable[[List[int]], None],
                  length_limit: int,
                  current: List = []) -> None:
    """
    Recursively generate all the possible keys for decrypting a vernam cipher
    :param callback: Called with all the inputs as they are generated
    :param length_limit: The longest inputs to generate, gives us the exit condition for recursion
    :param current: The current accumulated input
    """
    for a in range(len(ALPHABET)):
        next_input: List[int] = list(current)
        next_input.append(a)
        callback(next_input)
        if len(next_input) < length_limit:
            generate_keys(callback, length_limit, next_input)


def get_words_set(filename: str) -> Set[str]:
    """
    Given a file, reads each line as a single word and places it in the set
    :param filename: The filename to read, assumes the file contains one word per line
    :return: The set containing the words found in the file
    """
    words: Set[str] = set()
    with open(filename, 'r') as f:
        for line in [x.strip() for x in f]:
            words.add(line)

    return words


def try_key(cipher_text: str, key: List[int], words: Set[str]) -> float:
    """
    Given some cipher text and a key, it attempts to decrypt and analyse the
    generated plain text for likely success. It uses a dictionary of english words.
    Each word in the decrypted text is looked up in the english word set, and the decryption
    is scored by how many words match.

    :param cipher_text: The cipher text to decrypt
    :param key: The key to use
    :param words: The set of english words
    :return: A score for how many words in the decrypted plain text match english words. Score from 0.0 to 1.0
    """
    # Run the decryption
    cipher: VernamCipher = VernamCipher(key)
    potential_plain_text: str = cipher.decrypt(cipher_text)

    # Keep track of matching words, and total words
    matching_words: int = 0
    total_words: int = 0
    for word in potential_plain_text.split(" "):
        # If this word is in the set, count it
        if word in words:
            matching_words += 1
        total_words += 1

    # The score gives a proportion of words that appeared in the set
    hit_rate: float = matching_words / total_words

    return hit_rate


def get_keys(cipher_text: str,
             max_key_length: int,
             words_filename: str) -> Tuple[Optional[List[int]], float]:
    """
    Attempt brute force decryption of vernam cipher.

    :param cipher_text: The cipher text to decrypt
    :param max_key_length: The maximum key length to try, it will start from length 1.
    :param words_filename: The filename of words to use in the analysis
    :return: the most likely key, given matches against dictionary words
    """
    words: Set[str] = get_words_set(words_filename)
    keys: List[List[int]] = []

    # Generates all the possible keys, passing in the append function as the callback
    generate_keys(keys.append, max_key_length)

    # Keep track of the best score seen and it's corresponding key
    best_score: float = 0.0
    best_key: Optional[List[int]] = None
    for key in keys:
        score: float = try_key(cipher_text, key, words)
        # If every single word matched, just return immediately
        if score == 1.0:
            return key, 1.0
        # If we have a new best score, record it
        if score > best_score:
            best_score = score
            best_key = key

    # Return the best key found and it's score
    return best_key, best_score
