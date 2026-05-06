def is_valid_string(string: str, user_alphabet: list[str]) -> bool:
    # Reject duplicate strings
    if string in user_alphabet:
        print(f'Skipping: "{string}" is a duplicate.')
        return False

    # string is valid
    return True


def get_freq(string: str) -> int:
    while True:
        # Validate frequency
        try:
            freq: int = int(input(f'How many times does "{string}" occur? '))

            if freq <= 0:
                raise ValueError("Frequency can't be negative.")

            # Frequency is valid
            return freq
        except ValueError:
            print("Please enter an integer greater than zero.")


def gather_data() -> list[tuple[str, int]]:
    # Declare data structures
    user_alphabet: list[str] = []
    frequencies: list[int] = []

    while True:
        # Gather user input for string
        strings: list[str] = input("\nEnter a string (Press Enter to finish): ").split()

        # User presses Enter (finishes)
        if not strings:
            # Handle 1 string
            if len(user_alphabet) < 2:
                print("Program needs at least 2 strings to work.")
                continue
            # Finished successfully
            break

        for string in strings:
            if is_valid_string(string, user_alphabet):
                user_alphabet.append(string)

                # Gather user input for frequency
                freq = get_freq(string)
                frequencies.append(freq)

    # Create list of tuples from user_alphabet and frequencies
    tuples = list(zip(user_alphabet, frequencies))

    return tuples
