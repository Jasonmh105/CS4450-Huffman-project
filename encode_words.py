from Resources.huffman import huffman_algorithm
from Resources.display import display_final_table, display_welcome_msg
from Resources.user_input import gather_data

def encode_words() -> None:
    display_welcome_msg()

    elements = gather_data()

    # Compute huffman algorithm
    encoded_alphabet = huffman_algorithm(elements)

    display_final_table(encoded_alphabet)


def main():
    encode_words()


if __name__ == "__main__":
    main()
