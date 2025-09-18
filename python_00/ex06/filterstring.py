import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        words = sys.argv[1].split()
        min_length = int(sys.argv[2])
        fil_wrd = list(ft_filter(lambda word: len(word) > min_length, words))
        print(fil_wrd)

    except AssertionError as error:
        print(error)
    except ValueError:
        print("The third argument must be an integer.")


if __name__ == "__main__":
    main()
