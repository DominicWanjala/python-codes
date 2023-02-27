# a class to calculate the area and the perimeter of a rectangle
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+ self.width)
rect=rectangle(7,8)
print(rect.area())
print(rect.perimeter())
        


