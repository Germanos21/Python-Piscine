import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its format, shape, and pixel content in RGB format.
    Handles JPG and JPEG formats and provides clear error messages.

    Args:
    path (str): The path to the image file.

    Returns:
    np.ndarray: The image pixel data as a NumPy array.
    """
    try:
        img = Image.open(path)
        
        if img.format not in ["JPEG", "JPG"]:
            raise ValueError("Unsupported image format. Only JPG and JPEG are allowed.")
        
        print(f"The format of the image is: {img.format}")
        
        img_array = np.array(img)
        
        print(f"The shape of the image is: {img_array.shape}")
        
        return img_array
    
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

