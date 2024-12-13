# Create a Shape class with a method area() that 
# returns 0 by default. Derive two classes: Rectangle 
# (with attributes length and width) and Circle (with 
# attribute radius). Override the area() method in both 
# classes to calculate the respective areas

class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        result = self.length * self.width
        print(f"Area of Rectangle: {result}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        result = 3.14 * self.radius * self.radius
        print(f"Area of Circle: {result}")

shape1 = Rectangle(10,5)
shape1.area()

shape2 = Circle(4)
shape2.area()