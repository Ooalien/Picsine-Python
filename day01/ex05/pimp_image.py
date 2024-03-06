from array import array
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import copy



def show_image(array: array) -> None:
    ''' This function takes an array and displays the image.'''
    # image_array = format
    # sliced_image = image_array
    plt.imshow(array)
    plt.axis('off')  # Turn off axis
    plt.show()


def ft_invert(array) -> array:
    '''Inverts the color of the image received.'''
    show_image(255 - array)
    return array

def ft_red(array) -> array:
    '''Inverts the color of the image received to the red channel.'''
    tmp_array = copy.deepcopy(array)
    tmp_array[:, :, 1] = 0
    tmp_array[:, :, 2] = 0
    show_image(tmp_array)
    return array

def ft_green(array) -> array:
    '''Inverts the color of the image received to the green channel.'''
    tmp_array = copy.deepcopy(array)
    tmp_array[:, :, 0] = 0
    tmp_array[:, :, 2] = 0
    show_image(tmp_array)
    return array

def ft_blue(array) -> array:
    '''Inverts the color of the image received to the blue channel.'''
    tmp_array = copy.deepcopy(array)
    tmp_array[:, :, 0] = 0
    tmp_array[:, :, 1] = 0
    show_image(tmp_array)
    return array

def ft_grey(array) -> array:
    '''Inverts the color of the image received to the grey channel.'''
    tmp_array = copy.deepcopy(array)
    # gray_a rray = ( array[:,:,0] -  array[:,:,1] -  array[:,:,2]) / 3
    gray_array = np.zeros_like(array)
    tmp_array[:,:,1] = tmp_array[:,:,1]
    tmp_array[:,:,2] = tmp_array[:,:,2]
    tmp_array[:,:,0] = tmp_array[:,:,0]
    show_image(tmp_array)
    print(">>>>><<<<<<<")
    print(tmp_array)
    return array
