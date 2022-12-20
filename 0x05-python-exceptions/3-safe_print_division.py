#!/usr/bin/python3

def safe_print_division(a, b):
	answer = 0
	try:
		answer = a / b
		return (answer)
	except ZeroDivisionError:
		answer = None
		pass
	finally:
	 	print("Inside result: {}".format(answer))
