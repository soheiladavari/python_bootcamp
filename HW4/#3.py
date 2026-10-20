#3
class Shape:
    def __init__(self, name):
        self.name=name

    def area(self):
        return 0
    def area_info(self):
        print(f"shape:{self.name}, area:{self.area()}")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height   
import math
class Circle(Shape):
    def __init__(self ,radius):
        super().__init__("circle")
        self.radius=radius

    def area(self):
        return math.pi * self.radius**2

class Square(Rectangle):
    def __init__(self ,width):
        super().__init__(width, width)
        self.name="Square"


shapes=[Rectangle(4,5), Circle(3), Square(6)]
for shape in shapes:
    shape.area_info()

sq=Square(5)
print(isinstance(sq, Shape))
print(issubclass(Square, Shape))