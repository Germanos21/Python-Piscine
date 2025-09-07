import sys


def counter(arg):
    """
    Counts various types of characters in a given string.

    Args:
        arg (str): The input string to analyze.

    Returns:
        tuple: A tuple containing the counts of:
            - Total characters
            - Uppercase letters
            - Lowercase letters
            - Punctuation marks
            - Spaces
            - Digits
    """
    upper = 0
    lower = 0
    punct = 0
    total = 0
    space = 0
    digit = 0
    punct_str = '!"#$%&\'()*+,-./:;<=>?@[\\]^_``{|}~'

    for char in arg:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in punct_str:
            punct += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1
        total += 1
    return (total, upper, lower, punct, space, digit)


def main():
    """
    Main function to handle user input and display character counts.
    If a command-line argument is provided, it uses that as input.
    Otherwise, it prompts the user for input.
    """
    if (len(sys.argv) == 2):
        arg = sys.argv[1]
    elif (len(sys.argv) != 2):
        print("What is the text to count?")
        arg = input()

    count = counter(arg)
    print(f"The text contains {count[0]} characters:\n{count[1]} \
upper letters\n{count[2]} lower letters\n{count[3]} \
punctuation marks\n{count[4]} spaces\n{count[5]} digits")


if __name__ == "__main__":
    main()
