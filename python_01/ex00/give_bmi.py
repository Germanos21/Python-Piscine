import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for a list of heights and weights.

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[int | float]: A list of BMI values corresponding to the input
            heights and weights.

    Raises:
        ValueError: If the height and weight lists are not of the same size.
        TypeError: If any element in the height or weight lists is not an
            int or float.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same size.")
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("All elements in the height list must be int or float")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("All elements in the weight list must be int or float")

    height_np = np.array(height)
    weight_np = np.array(weight)
    bmi_np = weight_np / (height_np * height_np)
    return [float(bmi) for bmi in bmi_np]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMI values and return a list of booleans.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The BMI limit to compare against.

    Returns:
        list[bool]: A list of booleans where each element is True if the
            corresponding BMI value is greater than the limit, otherwise
            False.
    """
    return [bool(value) for value in (np.array(bmi) > limit)]
