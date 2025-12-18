with open("test.txt") as f:
	raw = f.read().strip()
	numbers = eval(raw)

print(f"numbers length: {len(numbers)}")

possible_combinations = []
pairs = []
for l1 in range(len(numbers) - 1):
	# print(f"l1: {l1}")
	for l2 in range(l1 + 1, len(numbers)):
		pairs.append([l1, l2, numbers[l1] + numbers[l2]])

pairs.sort(key=lambda v: v[2], reverse=1)
print(pairs)

# Find the different one
p1_i = 0
while p1_i < len(pairs) - 1:
	p2_i = p1_i + 1
	while p2_i < len(pairs) and pairs[p2_i][2] == pairs[p1_i][2]:
		print(f"Checking pair {pairs[p1_i]} to pair {pairs[p2_i]}")
		to_check = [pairs[p1_i][0], pairs[p1_i][1], pairs[p2_i][0], pairs[p2_i][1]]
		if sorted(list(set(to_check))) == sorted(to_check):
			print(f"Different: {to_check} => {pairs[p1_i][2]}")
			exit()
		p2_i += 1
	p1_i += 1
