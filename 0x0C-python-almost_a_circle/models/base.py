#!/usr/bin/python3

'''
this module is a base for all classes in the 0x0C project
'''

class Base:
	'''
		this class defines a base
	'''
	__nb_objects = 0   # private class attribute

	def __init__(self, id=None):
		'''
			initializes the Base class
		'''
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
