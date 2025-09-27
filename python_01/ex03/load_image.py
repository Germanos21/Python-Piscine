from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its format, and return its pixel content in RGB format.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: A NumPy array containing the pixel data in RGB format.

    Raises:
        ValueError: If the image format is not supported or if an error occurs.
    """
    try:
        im = Image.open(path)
        if im.format not in ["JPEG", "JPG"]:
            raise ValueError("Unsupported image format. Only JPG and JPEG are supported.")
        
        im = im.convert("RGB")
        pixel_data = np.array(im)
        print(f"The shape of image is: {pixel_data.shape}")
        return pixel_data

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")