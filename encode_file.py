import sys
from collections import Counter

from Algorithm.huffman import huffman_algorithm
from display import display_final_table

# Returns "GOODFILE" if file contains valid text, otherwise returns error code
def check_for_file_content():

    return_code = "GOODFILE"

    # Condition: only one argument given
    if (len(sys.argv) == 2):
        
        file_name = sys.argv[1]

        # Attempt to open and read file
        try:
            content = get_target_file_content()

            # Condition: file is empty
            if content == "":
                return_code = "ERROR: file is empty"
            
        except FileNotFoundError:
            return_code = "ERROR: file could not be read"

    # Condition: improper number of arguments given
    else:
        return_code = "USAGE: python encode_file.py <filename>"

    return(return_code)

# Reads file given in commandline argument, and returns contents as str
def get_target_file_content():

    file_name = sys.argv[1]
    file = open(file_name, 'r')
    content = file.read()
    file.close()

    return(content)

# Makes a new file with given name and content
def new_file(name, content):

    file_name = name

    file = open(file_name, 'w')
    file.write(content)
    file.close()

# Takes code tuples, and a given text, and returns text as codewords by character
def translate_text(key_tuples, orig_text):

    translated_text = ""

    for char in orig_text:
        for tuple in key_tuples:
            if char == tuple[0]:
                translated_text += tuple[2]

    return(translated_text)

# Converts given input string into list of tuples of each component character, and their frequency in the text
def count_chars(input_text):

    char_tuples = []

    # Returns dictionary with each char in input_text (<char> : <freq>)
    char_counts = Counter(input_text)
    # print(char_counts)

    # Converts char_counts to tuples
    for char,freq in char_counts.items():
        new_tuple = (char,freq)
        char_tuples.append(new_tuple)

    return(char_tuples)

# Takes file name as terminal arguement, and generates a new file with encoded text, as well as prints the decoding table
def encode_file():

    # verifies that file can be read, and contains encodable text
    file_validity = check_for_file_content()

    # Condition: file is valid for encoding
    if(file_validity == "GOODFILE"):

        file_content = get_target_file_content()

        # Convert from raw text to list of tuples able to be processed by huffman_algorithm()
        input_list = count_chars(file_content)

        # Compute huffman algorithm to return tuple list of codewords
        code_tuples = huffman_algorithm(input_list)

        # Generate encoded file name, and contents
        # File contents contain the list of code tuples, and the translated text
        new_file_name = "(encoded)_" + sys.argv[1]
        new_file_content = translate_text(code_tuples, file_content)

        # Display the decoding table to terminal
        print("YOUR ENCODED FILE IS LOCATED IN: ", new_file_name)
        display_final_table(code_tuples)

        # Make new file with translated text
        new_file(new_file_name, new_file_content)

    # Condition: file is not valid for encoding
    else:
        print(file_validity)

    return

def main():
    encode_file()

if __name__ == "__main__":
    main()
