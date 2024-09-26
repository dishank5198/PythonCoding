class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length*self.length


area1 = Shape()
print("Area of Shape: "+str(area1.area()))

area2 = Square(5)
print("Area of Square: "+str(area2.area()))