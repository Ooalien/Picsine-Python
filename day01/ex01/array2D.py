

def slice_me(family: list, start: int, end: int) -> list:
    ''' This function takes as parameters a 2D array, prints its shape, \
        and returns a truncated version of the array based on the \
        provided start and end arguments.'''
    print(f'My shape is : ({len(family)}, {len(family[0])})')
    family = family[start:end]
    print(f'My new shape is : ({len(family)}, {len(family[0])})')
    return [row for row in family]
