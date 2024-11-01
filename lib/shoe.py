class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Old"  # Initialize the condition attribute

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value > 0:
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  # Set condition to "New" after cobbling