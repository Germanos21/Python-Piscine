import sys

def is_integer(num):
    try:
        int(num)
        return (True)
    except ValueError:
        return (False)

if (len(sys.argv) == 1):
    exit
else:
    try:

        if (len(sys.argv) != 2):
            raise AssertionError("AssertionError: more than one argument is provided")
        if (is_integer(sys.argv[1]) == False):
            raise (AssertionError("AssertionError: argument is not an integer"))
        arg = int(sys.argv[1])
        if (arg % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as msg:
        print(msg)