from array import array
import numpy as np
from PIL import Image


def ft_load(path: str) -> array:
    ''' This function loads an image, prints its format, and its pixels \
        content in RGB format.'''
    try:
        img = Image.open(path)
        nparray = np.array(img)
        print(f'The shape of the image is: {nparray.shape}')
        return nparray
    except FileNotFoundError:
        return f'Error: file {path} not found'
