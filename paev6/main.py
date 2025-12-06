import re
import math

with open("input.txt") as f:
	line = f.readlines()[0].strip()

last_was_upper = False
length = 0
start_index = 0
longest_found_start = 0
longest_found_length = 0
for i, char in enumerate(line):
	if i == 0:
		last_was_upper = char.isupper()
		continue

	# Then it's all good! 
	if char.isupper() != last_was_upper:
		length += 1
		if length > longest_found_length:
			longest_found_length = length
			longest_found_start = start_index
		last_was_upper = char.isupper()
	elif char.isupper() == last_was_upper:
		start_index = i
		length = 0

print(longest_found_start, longest_found_length)
print(line[longest_found_start:longest_found_start + longest_found_length + 1])