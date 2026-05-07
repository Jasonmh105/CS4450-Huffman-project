from typing import Final

MAX_WORD_LEN: Final[int] = 14
MAX_FREQ_LEN: Final[int] = 9
TABLE_LEN: Final[int] = 34


def display_welcome_msg() -> None:
    print("""
==========================================================================
                       Welcome to Huffman Encoder!
==========================================================================

This program turns your alphabet into codewords using Huffman encoding.

To create your alphabet you'll be asked to input at least 2 strings (e.g.,
hello world). Each string is separated by a space. Then, for each string
you'll be asked to input how many times that string occurs (e.g, 42).
Finally, you'll see what your alphabet looks like when it is encoded!
""")


def display_final_table(encoded_alphabet: list[tuple[str, int, str]]) -> None:
    # Print column headers
    print("\n" + "-" * TABLE_LEN)
    print("Word           | Frequency | Code")
    print("-" * TABLE_LEN)

    for word, frequency, codeword in encoded_alphabet:
        frequency = str(frequency)

        # Truncate word if too long
        if len(word) > MAX_WORD_LEN:
            word = word[: MAX_WORD_LEN - 3] + "..."

        # Truncate frequency if too long
        if len(frequency) > MAX_FREQ_LEN:
            frequency = frequency[: MAX_FREQ_LEN - 3] + "..."

        # Display final rows
        print(f"{word:<{MAX_WORD_LEN}} | {frequency:<{MAX_FREQ_LEN}} | {codeword}")
