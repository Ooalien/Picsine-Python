from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def ft_zoom(path: str, factor: int) -> None:
    ''' This function takes a path to an image and a factor, and displays the \
        image zoomed by that factor.'''
    format = ft_load(path)
    print(format)
    new_height, new_width = 400, 400
    image_array = format
    start_row = (image_array.shape[0] - new_height) // factor
    start_col = (image_array.shape[1] - new_width) // factor
    # Slice the image
    sliced_image = image_array[start_row:start_row+new_height, start_col:start_col+new_width]

    print(f'New shape after slicing: {sliced_image.shape} or ({new_height}, {new_width})')

    print(sliced_image)
    # Display the sliced image
    plt.imshow(sliced_image)
    plt.axis('off')  # Turn off axis
    plt.show()

def main():
    ft_zoom('../../../animal.jpeg', 2)

if __name__ == "__main__":
    main()