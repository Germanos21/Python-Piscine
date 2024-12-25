import numpy as np


def validate_int(lst: list, name: str):
    """
    Validates that all elements in the given list are integers or floats.

    Args:
        lst (list): The list to validate.
        name (str): The name of the parameter being validated.

    Raises:
        ValueError: If any element in the list is not an integer or float.
    """
    if not all(isinstance(item, (int, float)) for item in lst):
        raise ValueError(f"Invalid input: {lst}")


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculates the BMI for given heights and weights.

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[int | float]: A list of calculated BMI values.

    Raises:
        ValueError: If the inputs are invalid, empty, or do not have the
        same size.
    """
    validate_int(height, "height")
    validate_int(weight, "weight")
    if not height or not weight:
        raise ValueError("No empty lists allowed")
    a = np.array(height)
    b = np.array(weight)
    if a.shape != b.shape:
        raise ValueError("Arrays must have the same size")
    a = a * height
    return (b / a).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applies a limit to a list of BMI values.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The limit to compare each BMI value against.

    Returns:
        list[bool]: A list of boolean values where True indicates that
        the BMI exceeds the limit.
    """
    return [value > limit for value in bmi]
