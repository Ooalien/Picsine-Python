from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Representing the King of the 7 kingdoms.'''
    
    def set_eyes(self, color):
        '''Set the color of the eyes.'''
        self.eyes = color

    def set_hairs(self, color):
        '''Set the color of the hairs.'''
        self.hairs = color

    def get_eyes(self):
        '''Get the color of the eyes.'''
        return self.eyes
    
    def get_hairs(self):
        '''Get the color of the hairs.'''
        return self.hairs