from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''
    def __init__(self, name, is_alive=True):
        super().__init__(name, is_alive)


class Lannister(Character):
    #your code here
    def __init__(self, name, is_alive=True):
        # f'''{'first_name': first_name, 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}'''
        super().__init__(name, is_alive)


# decorator
    def create_lannister(name, is_alive=True):
        return Lannister(name, is_alive)
