#!/usr/bin/python3

"""
Unittests for max_integers([..]).
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""
	defines unittests for max_integer([..]).
	"""

	def test_ordered_list(self):
		"""
		tests an ordered list of integers
		"""
		ordered = [1, 3, 5, 7]
		self.assertEqual(max_integer(ordered), 7)

	def test_unordered_list(self):
		"""
		tests an unordered list of integers
		"""
		unordered = [1, 3, 7, 5]
		self.assertEqual(max_integer(unordered), 7)

	def test_max_at_the_beginning(self):
		"""
		tests a list with max at the beginning
		"""
		max_at_the_beginning = [7, 5, 3, 1]
		self.assertEqual(max_integer(max_at_the_beginning), 7)

	def test_empty_list(self):
		"""
		test an empty list
		"""
		empty = []
		self.assertEqual(max_integer(empty), None)

	def test_one_element_list(self):
		"""
		tests a list with one element
		"""
		one_element = [3]
		self.assertequal(max_integer(one_element), 3)

	def test_floats(self):
		"""
		tests a list with floats
		"""
		floats = [3.4, 5.7, 9.0, -0.12, 23.9]
		self.assertEqual(max_integer(floats), 23.9)

	def test_ints_and_floats(self):
		"""
		tests a list with ints and floats
		"""
		ints_and_floats = [3.2, 4, 6.5, -2.5, 12]
		self.assertEqual(max_integer(ints_and_floats), 12)

	if __name__ == '__main__':
		unittest.main()
