"""
1. Let's say we make a class rectangle and a method to print the area.
2. Now I want one more shape and find it's area-Square.
What we can do here is that to have code reusability we can define a class setting rules to print area.
Such classes are called Abstract Classes.
Here we will make such a class like: Shape.
To make it an abstract class inport ABC, Abstractmethod from abc
3. Defining one more class-Circle.
This time not defining the function printarea inside it and defing print circumference
4. You cannot make an object of an abstract base class
"""
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def printarea(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def circumference(self):
        return 2*3.14*self.radius

    def printarea(self):
        return 4*3.14*self.radius*self.radius


rec1=Rectangle(10,6)
print(rec1.printarea())
cir1=Circle(10)
print(cir1.circumference())
print(cir1.printarea())