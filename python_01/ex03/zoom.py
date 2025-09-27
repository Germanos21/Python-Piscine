from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def main():
	loaded_img = ft_load('animal.jpeg')
	loaded_img = Image.convert('L')


if __name__ == '__main__':
	main()