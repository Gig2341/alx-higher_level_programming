#!/usr/bin/python3

def safe_print_division(a, b):
	try:
		answer = a / b
		return (answer)
	except ZeroDivisionError:
		pass
	finally:
	 	print("Inside result: {:f}".format(answer))
