import math


#No.1
class Apple:
    def __init__(self, c, l, b, p):
        self.color = c
        self.leaf = l
        self.brand = b
        self.price = p


#No.2
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius**2


circle1 = Circle(10)
print(circle1.area())


#No.3
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return  self.base * self.height * 0.5


triangle1 = Triangle(1, 2)
print(triangle1.area())


#No.4
class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_premieter(self):
        return  self.side*6


hexagon1 = Hexagon(2)
print(hexagon1.calculate_premieter())

