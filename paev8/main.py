import math
import re

def is_digit(n):
	try:
		int(n)
		return True
	except ValueError:
		return False

with open("test.txt") as f:
	raw = f.read().strip()
	lines = raw.split("\n")

longest_length = 0
for line_i, line in enumerate(lines):
	started = False
	length = 0
	for char_i, char in enumerate(line):
		if char != '*' and started == False:
			started = True
			length = 1
		elif char == '*':
			started = False
			length = 0
		elif char != '*' and started == True:
			length += 1
		# print(char, length)
		if length > longest_length:
			longest_length = length

for line in lines:
	print(line)

print()

lines = list(zip(*lines[::-1]))
for line in lines:
	print(line)

for line_i, line in enumerate(lines):
	started = False
	length = 0
	for char_i, char in enumerate(line):
		if char != '*' and started == False:
			started = True
			length = 1
		elif char == '*':
			started = False
			length = 0
		elif char != '*' and started == True:
			length += 1
		# print(char, length)
		if length > longest_length:
			longest_length = length

print(longest_length)

