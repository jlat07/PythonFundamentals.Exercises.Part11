

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def area(self):
        a = self.length * self.width
        return a

    def perimeter(self):
        p = (self.length + self.width)*2
        return p

class Square(Rectangle):
    def __init__(self, length: int):
        super().__init__(length, length)
    
    


rect = Rectangle(2, 4)
rect.area()
# 8

square = shapes.Square(8)
square.area()
# 64

square.perimeter()
# 32
```