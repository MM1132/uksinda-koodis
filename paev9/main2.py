import re
import math

with open("test.txt") as f:
	raw = f.read().strip()

one_line = list(map(int, re.split(r'[\n ]', raw)))
print(one_line)

room_number = one_line[0]
print(room_number)

for i in range(2, len(one_line), 2):
	if room_number == one_line[i]:
		room_number = one_line[i + 1]
	elif room_number == one_line[i + 1]:
		room_number = one_line[i]

print(room_number)
