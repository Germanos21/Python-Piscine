def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        raise ValueError("Input must be a 2D list.")
    if len(set(len(row) for row in family)) != 1:
        raise ValueError("All rows in the 2D list must have the same size.")
    
    # Print the original shape
    rows = len(family)
    cols = len(family[0])
    print(f"My shape is : ({rows}, {cols})")
    
    truncated_family = family[start:end]
    
    new_rows = len(truncated_family)
    print(f"My new shape is : ({new_rows}, {cols})")
    
    return truncated_family