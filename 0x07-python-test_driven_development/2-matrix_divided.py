#!/usr/env/python3

def matrix_divided(matrix, div):
	"""
	"""

	if not matrix or not isinstance (matrix, list):
		raise TypeError("matrix must be a matrix (lists of lists) of integers/floats")
	if type(div) is not int and type(div) is not float:
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")

	length_row = len(matrix[0])
	for row in matrix:
		if type(row) is not list:
			raise TypeError
		if len(row) != length_row:
			raise TypeError
		for column in row:
			if type(column) is not int and type(column) is not float:
				raise TypeError
	new_matrix = list(map(lambda x : list(map(lambda y : round(y/div, 2), x)), matrix))
	return new_matrix
