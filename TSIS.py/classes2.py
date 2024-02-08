class Shape:
    def area(self, a = 0):
        print(a)
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length * self.length)
p1 = Shape()#p1 is an object of class
p2 = Square(5)#p2 is an objec of a subclass
p1.area()
p2.area()

""""
Shape - class has an area that returns 0
Square - subclass of a shape and area calculates the area of a square.
Square class has an init method that takes the length of the square as an argument
"""