import time
from typing import List, Optional

from CORE_DataRepresentation.VernamCipher import VernamCipher, generate_one_time_pad
from CORE_DataRepresentation.BreakVernamCipher import get_keys

WORDS_FILENAME: str = 'words_alpha.txt'
BENCHMARK_RESULTS_FILENAME = 'brute_force.csv'

plain_text: str = 'ive got a brand new combine harvester and I gave you the key'

with open(BENCHMARK_RESULTS_FILENAME, 'w') as f:
    f.write("Key Length,Milliseconds\n")
    for key_length in range(1, 5):
        # Generate a key, then encrypt the data
        key: List[int] = generate_one_time_pad(key_length)
        my_cipher: VernamCipher = VernamCipher(key)
        my_cipher_text: str = my_cipher.encrypt(plain_text)

        # Do a timed run on brute force decryption
        print("Attempting brute force decryption for key length {}".format(key_length), end="...")
        start_time = time.process_time_ns()
        found_key, score = get_keys(my_cipher_text, len(key), WORDS_FILENAME)
        time_taken_ms: int = (time.process_time_ns() - start_time) // 1000000
        print("Done in {} ms".format(time_taken_ms))

        # Write the CSV line
        f.write("{},{}\n".format(key_length, time_taken_ms))
