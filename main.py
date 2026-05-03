from Algorithm.huffman import huffman_algorithm
from display import display_final_table, display_welcome_msg
from user_input import gather_data

# Dummy data for testing purposes
# def gather_data():
#     # Gather Input Data
#     user_alphabet = ["this", "is", "an", "alphabet", "of", "strings"]
#     freq_dis = [34, 6, 75, 2, 56, 18]

#     # Combine lists using tuples (ensures association during sorting)
#     alpha_freq_list = zip(user_alphabet, freq_dis)

#     return alpha_freq_list


def main():
    display_welcome_msg()

    elements = gather_data()

    # Compute huffman algorithm
    encoded_alphabet = huffman_algorithm(elements)

    # Display results
    print("PRINTING FINAL ENCODED ALPHABET:     ", encoded_alphabet)

    display_final_table(encoded_alphabet)


if __name__ == "__main__":
    main()
