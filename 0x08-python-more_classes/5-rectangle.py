#!/usr/bin/python3

"""
this module defines a rectangle
"""


class Rectangle:
    """
    this class represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        this method initializes the class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is negative
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        this method retrieves the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        this method sets the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        this method retreives the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this method sets the height of the Rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        this method returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        this method returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        p = (self.__height + self.__width) * 2
        return p

    def __str__(self) -> str:
        """
        this method returns a diagram of the rectangle in terms of '#'
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """
        this method returns a string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        this method prints a message when an instance of a rectangle
        is deleted
        """
        print("Bye rectangle...")
