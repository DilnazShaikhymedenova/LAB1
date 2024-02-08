class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x},{self.y})")
    def move(self):
        self.x = int(input("new x coordinate: "))
        self.y = int(input("new y coordinate: "))
    def dist(self, obj):
        print ((((obj.x - self.x)**2) + ((obj.y - self.y)**2))**0.5)
p1 = Point(2, 4)#added point 1
p2 = Point(5, 6)#added point 2
p1.show()#see the coordinates of point 1
p1.move()#change the coordinates of point 1
p1.show()#see how the coordinates of point 1 have changed
p2.show()#see the coordinates of point 2
p1.dist(p2)#see the distance between point 1 and point 2