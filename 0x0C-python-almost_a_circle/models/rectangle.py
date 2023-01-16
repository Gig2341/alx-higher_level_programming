#!/usr/bin/python3
from models.base import Base

'''
this module represents a rectangle that inherits from the base class
'''

class Rectangle(Base):
	'''
		this class defines a rectangle
		
	'''

	def __init__(self, width, height, x=0, y=0, id=None):
		'''
			initializes the rectangle class
		'''

		super().__init__(id)
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y

		@property
		def width(self):
			'''
				 setter method for width
				 Return: width
			'''
			return self.__width

		@width.setter
		def width_setter(self, value):
			'''
				getter method for width
				Args:
					value(int) to be set
			'''
			if type(value) is not int:
				raise TypeError("width must be an integer")
			elif value <= 0:
				raise ValueError("width must be >= 0")
			else:
				self.__width = value

		@property
		def height(self):
			'''
				setter method for height
				Return: height
			'''
			return self.__height

		@width.setter
		def height_setter(self, value):
			'''
				getter method for height
				Args:
					value(int) to be set
			'''
			if type(value) is not int:
				raise TypeError("height must be an integer")
			elif value <= 0:
			 	raise ValueError("height must be >= 0")
			else:
				self.__height = value

		@property
		def x(self):
			'''
				getter method for x
				Return: x
			'''
			return self.__x

		@x.setter
		def x_setter(self, value):
			'''
				setter method for x
				Args: value(int) to be set
			'''
			if type(value) is not int:
				raise TypeError("x must be an integer")
			elif value <= 0:
				raise ValueError("x must be >= 0")
			else:
				self.__x = value

		@property
		def y(self):
			'''
				getter method for y
				Return: y
			'''
			return self.__y
		
		@y.setter
		def y(self, value):
			'''
				setter method for y
				Args: value(int) to be set
			'''
			if type(value) is not int:
				raise TypeError("y must be an integer")
			elif value <= 0:
				raise ValueError("y must be >= 0")

			else:
				self.__y = value

		def area(self):
			'''Method that returns the area of the rectangle object
			   Return: Area of the rectangle object
			'''
			return self.__width * self.__height

		def display(self):
			'''
				method that prints to stdout
				rectangle object with the character #
			'''
			for i in range(self.__
