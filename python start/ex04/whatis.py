import sys

if len(sys.argv) == 1:
    print()
    sys.exit()
assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
try:
    number = int(sys.argv[1])
except ValueError:
    raise AssertionError("AssertionError: argument is not an integer")
print("I'm Even.") if number % 2 == 0 else print("I'm Odd.")
