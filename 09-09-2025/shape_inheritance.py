class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,l):
        self.l=l
    def area(self):
        return self.l*self.l
sq=Square(7)
print("Area of square = ",sq.area())