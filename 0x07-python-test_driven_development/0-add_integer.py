#!/usr/bin/python3

'''

This module has a function that adds numbers

'''

def add_integer(a, b=98):
	'''
	This function adds two numbers.

	Args: 
		a: first number
		b: second number

	Returns:
		the sum of the two numbers
	
	Raises:
		TypeError: If a or b aren't integer and/or float numbers
	'''
	
	if not isinstance(a,int) and if not isinstance(a, float):
		raise TypeError("a must be an integer")
	if not isinstance(b,int) and if not isinstance(b, float):
		raise TypeError("b must be an integer")

	return(a + b) 
