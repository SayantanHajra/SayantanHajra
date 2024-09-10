class Rectangle:
    def __init__(self, length: int, width: int):
        if not isinstance(length, int) or not isinstance(width, int):
            raise TypeError("Length and width should be integers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width can't be negative")
        
        self.length = length
        self.width = width

    def __iter__(self):
        return iter((self.length, self.width))

    def __str__(self):
        return f"{{'length': {self.length}}} followed by the width {{'width': {self.width}}}"

rect = Rectangle(20, 15)

print(str(rect))

for value in rect:
    print(value)





