#!/usr/bin/python3

class Square:
	try:
		def __init__(self, size=0):
			'''initializes a square
			Args: size - represents the size of the square'''
			self.__size = size   

	except TypeError:
		print("size must be an integer")
	except ValueError:
		print("size must be >= 0")
