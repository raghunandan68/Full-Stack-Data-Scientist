class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, name,w,h):
        super().__init__(name)
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
class Circle(Shape):
    def __init__(self, name,r):
        super().__init__(name)
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
c=Circle("c1",7)
print("Area of circle = ",c.area())
r = Rectangle("r1",4, 5)
print("Area of rectangle = ",r.area())