from Algorithm.huffman import huffman_algorithm
from user_input import gather_data

# Dummy data for testing purposes
# def gather_data():
#     # Gather Input Data
#     user_alphabet = ["this", "is", "an", "alphabet", "of", "strings"]
#     freq_dis = [34, 6, 75, 2, 56, 18]

#     # Combine lists using tuples (ensures association during sorting)
#     alpha_freq_list = zip(user_alphabet, freq_dis)

#     return alpha_freq_list


def display_welcome_msg() -> None:
    print("""
==========================================================================
                       Welcome to Huffman Encoder!
==========================================================================

This program turns your alphabet into codewords using Huffman encoding.

To create your alphabet you'll be asked to input at least 2 strings (e.g.,
hello world). Each string is separated by a space. Then, for each string
you will be asked to input how many times that string occurs (e.g, 42).
Finally, you will see what your alphabet looks like when it is encoded!
""")


def main():
    display_welcome_msg()

    elements = gather_data()

    # Compute huffman algorithm
    encoded_alphabet = huffman_algorithm(elements)

    # Display results
    print("PRINTING FINAL ENCODED ALPHABET:     ", encoded_alphabet)


if __name__ == "__main__":
    main()

