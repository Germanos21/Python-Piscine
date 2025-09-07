def ft_filter(iterable, condition):
    """
    Filters elements from an iterable based on a condition.

    Args:
        iterable (iterable): The input iterable to filter.
        condition (function): A function that returns True for elements to keep

    Returns:
        list: A list of elements that satisfy the condition.
    """
    return [item for item in iterable if condition(item)]


def is_even(x):
    """
    Checks if a number is even.

    Args:
        x (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return x % 2 == 0


def main():
    """
    Demonstrates the usage of ft_filter by filtering even numbers from a list.
    """
    numbers = [1, 2, 3, 4, 5, 6]
    result = ft_filter(numbers, is_even)
    print("Filtered result:", result)


if __name__ == "__main__":
    main()
