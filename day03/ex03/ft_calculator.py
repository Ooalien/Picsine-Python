class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar):
        result = [x + scalar for x in self.vector]
        print(result)
        self.vector = result
        return result

    def __mul__(self, scalar):
        result = [x * scalar for x in self.vector]
        print(result)
        self.vector = result    
        return result

    def __sub__(self, scalar):
        result = [x - scalar for x in self.vector]
        print(result)
        self.vector = result
        return result

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        result = [x / scalar for x in self.vector]
        self.vector = result
        print(result)
        return result
