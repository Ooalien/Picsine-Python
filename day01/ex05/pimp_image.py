from array import array
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


def ft_grey(a) -> array:
    '''Inverts the color of the image received to the grey channel.'''
    t = copy.deepcopy(a)
    t[:, :, 0] = \
        np.sum(a[:, :, :3] / np.array([1/0.2989, 1/0.5870, 1/0.1140]), axis=2)
    t[:, :, 1] = \
        np.sum(a[:, :, :3] / np.array([1/0.2989, 1/0.5870, 1/0.1140]), axis=2)
    t[:, :, 2] = \
        np.sum(a[:, :, :3] / np.array([1/0.2989, 1/0.5870, 1/0.1140]), axis=2)
    show_image(t)
    return array
