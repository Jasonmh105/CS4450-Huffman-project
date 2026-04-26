from Algorithm.huffman import huffmanAlgorithm

def main():
    
    # Gather Input Data
    user_alphabet = ["this", "is", "an", "alphabet", "of", "strings"]
    freq_dis = [34, 6, 75, 2, 56, 18]

    # Compute huffman algorithm
    # encoded_alphabet = huffmanAlgorithm(user_alphabet, freq_dis)

    # Temp
    huffmanAlgorithm(user_alphabet,freq_dis)

    # Display results
    for i in range(0, len(user_alphabet)):
        # when implemented, change to print(user_alphabet[i], freq_dis[i], encoded_alphabet[i])
        print(user_alphabet[i], freq_dis[i])

if __name__ == "__main__":
    main()