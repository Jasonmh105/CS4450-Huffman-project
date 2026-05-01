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

def main():
    
    elements = gather_data()
    
    # Compute huffman algorithm
    encoded_alphabet = huffman_algorithm(elements)

    # Display results
    print("PRINTING FINAL ENCODED ALPHABET:     ", encoded_alphabet)

if __name__ == "__main__":
    main()