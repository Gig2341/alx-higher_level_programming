#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	'''a function that prints x elements of a list.
	my_list can contain any type (integer, string, etc.)
	x represents the number of elements to print
	x can be bigger than the length of my_list
	Returns the real number of elements printed'''

	total = 0
	for i in range(x):
		try:
			print(f"{my_list[i]}", end="")
			total += 1
		except IndexError:
			break
	print()
	return(total)
