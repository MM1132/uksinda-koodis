with open("input.txt") as f:
	raw = f.read().strip()
	numbers = [int(n.strip()) for n in raw.split(" ")]

longest_chains = [None] * len(numbers)

def get_depth_from_index(last_number, start_i = 0, depth = 1):
	# So you take our current number and you add it to the list
	# if it is bigger than the last one, or the list has no elements
	# then we add it into the list, and move onto the next number

	# If we reach the end of the list, save the length of the array
	# then for our function we change the 

	# print("in index", start_i, "with depth")

	depths = []
	for i in range(start_i + 1, len(numbers)):
		if numbers[i] >= last_number:
			if longest_chains[i] is not None:
				depths.append(longest_chains[i])
				continue

			print(numbers[i], "is bigger than", last_number)
			d = get_depth_from_index(numbers[i], i)
			longest_chains[i] = d

			# print(f"Number: {numbers[i]}, Index: {i}, Depth: {d}")
			depths.append(d)
			# print(depths)
	if len(depths) > 0:
		return max(depths) + 1
	return depth

for index in range(len(numbers)):
	longest_chains[index] = get_depth_from_index(numbers[index], index)

print(longest_chains)

longest = max(filter(lambda v: v is not None, longest_chains))
print(f"longest chain: {longest}")
print(len(numbers) - longest)

# print(numbers)
