from math import pi
from abc import ABC, abstractmethod, ABCMeta


class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area (self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.__r = radius

    def calculate_perimeter(self):
        result = pi * 2 * self.__r
        return result

    def calculate_area (self):
        result = pi * (self.__r ** 2)
        return  result


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calculate_perimeter(self):
        result = 2 * (self.__width + self.__height)
        return result

    def calculate_area (self):
        result = self.__height * self.__width
        return  result


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

