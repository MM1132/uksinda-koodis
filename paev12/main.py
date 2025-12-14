with open("input.txt") as f:
	raw = f.read().strip()
	numbers = [int(n.strip()) for n in raw.split(" ")]

all_found_depths = [None] * len(numbers)

def get_depth_from_index(last_number, start_i = 0, depth = 1):
	depths = []
	for i in range(start_i + 1, len(numbers)):
		if numbers[i] >= last_number:
			if all_found_depths[i] is None:
				all_found_depths[i] = get_depth_from_index(numbers[i], i)

			# print(numbers[i], "is bigger than", last_number)
			# print(f"Number: {numbers[i]}, Index: {i}, Depth: {d}")
			
			depths.append(all_found_depths[i])
			
			# print(depths)
	if len(depths) > 0:
		return max(depths) + 1
	return depth

for index in range(len(numbers)):
	if all_found_depths[index] is None:
		all_found_depths[index] = get_depth_from_index(numbers[index], index)

print(all_found_depths)

longest = max(filter(lambda v: v is not None, all_found_depths))
print(f"longest chain: {longest}")

print(len(numbers) - longest)
