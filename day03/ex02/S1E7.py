from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    family_name = 'Baratheon'
    eyes = 'brown'
    hairs = 'dark'

    def __init__(self, name, is_alive=True):
        super().__init__(name, is_alive)
        self.__dict__.update({'family_name': self.family_name, 'eyes': self.eyes, 'hairs': self.hairs})

    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"


class Lannister(Character):
    """Representing the Lannister family."""
    family_name = 'Lannister'
    eyes = 'blue'
    hairs = 'light'

    def __init__(self, name, is_alive=True):
        super().__init__(name, is_alive)
        self.__dict__.update({'family_name': self.family_name, 'eyes': self.eyes, 'hairs': self.hairs})


    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"
    
    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def create_lannister(name, is_alive=True):
        return Lannister(name, is_alive)
