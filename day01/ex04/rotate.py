from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(path: str, factor: int) -> None:
    ''' This function takes a path to an image and a factor, and displays the \
        image zoomed by that factor.'''
    format = ft_load(path)
    print(format)
    array = format
    start = (array.shape[0] - 400) // factor
    start_col = (array.shape[1] - 400) // factor
    sliced_image = array[start:start+400, start_col:start_col+400]
    print(f'New shape after slicing: {sliced_image.shape} or ({400}, {400})')
    sliced_image = list(zip(*sliced_image[::-1]))
    plt.imshow(sliced_image)
    plt.axis('off')
    plt.show()


def main():
    ft_zoom('../../../animal.jpeg', 2)


if __name__ == "__main__":
    main()
