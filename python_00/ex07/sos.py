import sys


MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}


def main():
    try:
        assert len(sys.argv) == 2, "AssertionError: the program takes \
exactly one argument."

        input_arg = sys.argv[1].upper()

        if not all(char in MORSE_CODE_DICT for char in input_arg):
            raise AssertionError("AssertionError: the argument contains \
invalid characters.")

        morse_code = ' '.join(MORSE_CODE_DICT[char] for char in input_arg)
        print(morse_code)

    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
