import sys
from ft_filter import ft_filter


def filter_words(S, N):
    return list(ft_filter(lambda word: len(word) > N, S.split()))


def main():
    if (len(sys.argv) != 3):
        raise AssertionError("the arguments are bad")

    S = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    if not isinstance(S, str) or not isinstance(N, int):
        raise AssertionError("the arguments are bad")

    print(filter_words(S, N))


if __name__ == "__main__":
    main()
