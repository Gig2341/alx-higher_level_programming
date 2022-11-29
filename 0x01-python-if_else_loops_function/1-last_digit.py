#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number % 10 > 5)
	print(f"Last digit of {number:d} is {number % 10 > 5:d} and is greater than 5")
elif (number % 10 < 6)
	print(f"Last digit of {number:d} is {number % 10 > 5:d} and is less than 6 but not zero")
else
	print(f"Last digit of {number:d} is {number % 10 > 5:d} and is 0")
