import sys


def counter(text):

    lchar = 0
    uchar = 0
    spaces = 0
    punct = 0
    digits = 0

    for c in text:
        if c.islower():
            lchar += 1
        elif c.isupper():
            uchar += 1
        elif c.isspace():
            spaces += 1
        elif c.isdigit():
            digits += 1
        elif not c.isalpha():
            punct += 1

    chars = [uchar, lchar, punct, digits, spaces]
    return (chars)


def print_chars(lst):
    print(f'{lst[0]} upper letters')
    print(f'{lst[1]} lower letters')
    print(f'{lst[2]} punctuation marks')
    print(f'{lst[3]} digits')
    print(f'{lst[4]} spaces')


def main():
    assert len(sys.argv) <= 2, "must have zero or one arguments."

    if len(sys.argv) == 1:
        text = input("Please provide the text: ")
    else:
        text = sys.argv[1]
    print(f'The text contains {len(text)} characters:')
    broken_chars = counter(text)
    print_chars(broken_chars)


if __name__ == "__main__":
    main()
