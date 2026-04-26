from Algorithm.huffman import huffmanAlgorithm

def gatherData():
    # Gather Input Data
    user_alphabet = ["this", "is", "an", "alphabet", "of", "strings"]
    freq_dis = [34, 6, 75, 2, 56, 18]

    # Combine lists using tuples (ensures association during sorting)
    alpha_freq_list = []
    for i in range(0,len(user_alphabet)):
        alpha_freq_list.append((user_alphabet[i], freq_dis[i]))

    return alpha_freq_list

def main():
    
    elements = gatherData()
    
    # Compute huffman algorithm
    encoded_alphabet = huffmanAlgorithm(elements)

    # Display results
    print(encoded_alphabet)

if __name__ == "__main__":
    main()