class Triangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height / 2.0
        return area

class Square:
    def __init__(self,size):
        self.size = size

    def getArea(self):
        area = self.size*self.size
        return  area
myTriangle = Triangle(4,5)
b = Square(5)
myTriangle.getArea()


