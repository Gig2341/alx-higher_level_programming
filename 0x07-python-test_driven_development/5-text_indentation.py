#!/usr/bin/python3

"""
this module indents a text after each '.,?,:'
"""

def text_indentation(text):
	"""
	this method indents a text after each '.,?,:'
	"""

	if not isinstance(text, str):
		raise TypeError("text must be a string")
	
	character_count = 0

	while character_count < len(text) and text[character_count] == " ":
		character_count += 1

	while character_count < len(text):
		print(text[character_count], end="")
		if text[character_count] == "\n" or text[character_count] in ".?:":
			if text[character_count] in ".?:":
				print("\n")
			character_count += 1
			while character_count < len(text) and text[character_count] == " ":
				character_count += 1
			continue
		character_count += 1
