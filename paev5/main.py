import math
import re

with open("test.txt") as f:
	lines = [line.strip() for line in f.readlines()]

coordinates = []

def add_to_coordinates(y, x):
	global coordinates

	if x < 3:
		x += 1
	elif x > 8:
		x -= 1

	coordinates.append((y + 1, x))

for line_i, line in enumerate(lines):
	line_len = len(line)
	for i, char in enumerate(line):
		if char != "0":
			continue

		print("x: ", i)

		if i == 0:
			if line[i + 1] == "0":
				add_to_coordinates(line_i, i)
		elif i == line_len - 1:
			if line[i - 1] == "0":
				add_to_coordinates(line_i, i)
		else:
			if line[i - 1] == "0" or line[i - 1] == " ":
				if line[i + 1] == "0" or line[i + 1] == " ":
					add_to_coordinates(line_i, i)

print(coordinates)
