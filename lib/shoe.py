class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  
        self.size = size  
        self.condition = "Used"  

    
    def size(self):
        return self._size

    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
