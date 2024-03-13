from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(path: str, factor: int) -> None:
    ''' This function takes a path to an image and a factor, and displays the \
        image zoomed by that factor.'''
    format = ft_load(path)
    print(format)
    h, w = 400, 400
    image_array = format
    start_row = (image_array.shape[0] - h) // factor
    start_col = (image_array.shape[1] - w) // factor
    sliced_image = image_array[start_row:start_row+h, start_col:start_col+w]
    print(f'New shape after slicing: {sliced_image.shape} or ({h}, \
          {w})')
    print(sliced_image)
    plt.imshow(sliced_image)
    plt.axis('off')
    plt.show()


def main():
    ft_zoom('../../../animal.jpeg', 2)


if __name__ == "__main__":
    main()
