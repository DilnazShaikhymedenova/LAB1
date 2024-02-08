class Shape:
    def area(self, a = 0):
        print(a)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
p1 = Rectangle(4, 5)#p1 is an object of a Rectangle subclass
p2 = Shape()#p2 is an object of a class Shape
p1.area()
p2.area()
