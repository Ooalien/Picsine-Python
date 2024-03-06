

def give_bmi(height: list[int | float], weight: list[int | float]) -> \
        list[int | float]:
    ''' This function takes in two lists of integers or floats,
        height and weight, and returns a list of BMI values.'''
    if len(height) != len(weight):
        return 'Error: height and weight lists must have the same length'
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            return 'Error: height and weight values must be integers or floats'
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ''' This function takes in a list of BMI values and a limit, and returns \
        a list of booleans indicating whether each BMI value is greater than \
        or equal to the limit.'''
    return [b >= limit for b in bmi]
