import re
import math

with open("test.txt") as f:
	raw = f.read().strip()
	lines = raw.split("\n")

room_number = int(lines[0].split(" ")[0])

for line in [[int(n) for n in line.split(" ")] for line in lines[1:]]:
	print(line)

	first_numbers = line[0::2]
	second_numbers = line[1::2]
	
	for i in range(len(first_numbers)):
		if room_number == first_numbers[i]:
			room_number = second_numbers[i]
		elif room_number == second_numbers[i]:
			room_number = first_numbers[i]

print(room_number)
