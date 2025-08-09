def ft_filter(condition_function, iterable):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return (item for item in iterable if condition_function(item))


if __name__ == "__main__":
    print(ft_filter.__doc__)
    print(filter.__doc__)
    tmp = ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(tmp))
    print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
