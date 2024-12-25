import sys


def count_characters(text):
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    digit_count = 0
    space_count = 0

    punctuation_chars = '.?!,;:-{}[]?\"\'`'

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in punctuation_chars:
            punctuation_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    if (len(sys.argv) == 1):
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        raise AssertionError("AssertionError: more than one argument")

    count_characters(text)


if __name__ == "__main__":
    main()
