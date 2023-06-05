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
		"""
	self.width = width
	self.height = height

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
