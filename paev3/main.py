import math

with open("test.txt") as f:
	lines = [line.strip() for line in f.readlines()]
	max_weight = int(lines[0])
	gift_weights = [int(line) for line in lines[1].split(",")]
	gift_weights = sorted(gift_weights)
	print(gift_weights)

total_weight = 0
total_gifts = 0
for g in gift_weights:
	if total_weight < max_weight and total_weight + g < max_weight:
		# print("adding", g, "to", total_weight)
		total_weight += g
		total_gifts += 1
		# print("total is now", total_weight)

print(total_gifts)
