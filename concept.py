from abc import ABC, abstractmethod
class Shape(ABC):
    
    @abstractmethod
    def area (self):
        pass

class Rectangel(Shape):
      

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length* self.breadth
    
class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 7.14 * self.radius * self.radius

rec = Rectangel(12,8)
cir = Circle(9)

#rec.area
#cir.area
shapes = [ rec,cir]
for shape in shapes:
    print("area==",shape.area())

