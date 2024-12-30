from typing import Any, Callable

def callLimit(limit: int) -> Callable:
    """
    This function takes an argument 'limit', which defines the maximum number of times
    a decorated function can be called. If the function is called more than the limit,
    it raises an error.
    """
    def callLimiter(function: Callable) -> Callable:
        count = 0  # Initialize a counter to keep track of how many times the function is called.
        
        def limit_function(*args: Any, **kwargs: Any) -> None:
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)  # Execute the function if the call count is below the limit.
            else:
                print(f"Error: {function} call too many times")  # Print an error if the limit is exceeded.
        
        return limit_function  # Return the wrapped function.
    
    return callLimiter  # Return the decorator.
