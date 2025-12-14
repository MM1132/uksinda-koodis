import math
import re

def is_digit(n):
	try:
		int(n)
		return True
	except ValueError:
		return False

with open("input.txt") as f:
	raw = f.read().strip()
	numbers = eval(raw)

print(f"numbers length: {len(numbers)}")

possible_combinations = []
pairs = []
for l1 in range(len(numbers) - 1):
	print(f"l1: {l1}")
	for l2 in range(l1 + 1, len(numbers)):
		pairs.append([l1, l2, numbers[l1] + numbers[l2]])
		# for r1 in range(len(numbers) - 1):
		# 	for r2 in range(r1 + 1, len(numbers)):
		# 		# If none of them overlap
		# 		if list(set([l1, l2, r1, r2])) == sorted([l1, l2, r1, r2]):
		# 			# print(f"{l1}, {l2}, {r1}, {r2}")
		# 			if numbers[l1] + numbers[l2] == numbers[r1] + numbers[r2]:
		# 				possible_combinations.append(numbers[l1] + numbers[l2])

# for pair in pairs:
# 	print(f"{pair[0]} + {pair[1]} = {pair[2]}")

pairs.sort(key=lambda v: v[2], reverse=1)

# print(f"pairs sorted: {pairs}")

p1_i = 0
while p1_i < len(pairs) - 1:
	p2_i = p1_i + 1
	while p2_i < len(pairs) and pairs[p2_i][2] == pairs[p1_i][2]:
		print(f"Checking pair {pairs[p1_i]} to pair {pairs[p2_i]}")
		to_check = [pairs[p1_i][0], pairs[p1_i][1], pairs[p2_i][0], pairs[p2_i][1]]
		# If all of the numbers are different
		if sorted(list(set(to_check))) == sorted(to_check):
			print(f"Different: {to_check} => {pairs[p1_i][2]}")
			exit()
		p2_i += 1
	p1_i += 1

# print(f"max of possible combinations: {max(possible_combinations)}")
