def square(x: int | float) -> int | float:
    """
    Returns the square of the argument.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Returns the result of raising the argument to the power of itself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Takes a number and a function as arguments, and returns an object (function) that,
    when called, applies the function repeatedly to the result of previous calls.
    """
    count = x
    
    def inner() -> float:
        nonlocal count
        count = function(count)
        return count
    
    return inner
