<h1 align="center">Huffman Encoder</h1>

## Overview

This project implements the Huffman Encoding algorithm in Python. It takes an alphabet of elements (either user-inputted strings or characters from a text file) along with their frequency distributions, and generates a table of binary prefix codewords. This encoding minimizes the average bits used per element, effectively compressing the data.

## Usage

You can use the Huffman encoder in two ways:

1. Interactively:
```bash
python encode_words.py
```

2. Or by running it on a file:
``` bash
python encode_file.py <filename.txt>
```

### Example Output (Interactive)
```bash
Enter a string (Press Enter to finish): hello world and all who inhabit it
How many times does "hello" occur? 40
How many times does "world" occur? 322
How many times does "and" occur? 55
How many times does "all" occur? 8888
How many times does "who" occur? 9
How many times does "inhabit" occur? 1
How many times does "it" occur? 321235

Enter a string (Press Enter to finish):

----------------------------------
Word           | Frequency | Code
----------------------------------
inhabit        | 1         | 000000
who            | 9         | 000001
hello          | 40        | 00001
and            | 55        | 0001
world          | 322       | 001
all            | 8888      | 01
it             | 321235    | 1
```
