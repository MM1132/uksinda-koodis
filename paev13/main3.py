with open("input.txt") as f:
	line = f.read().strip()

line = line[1:]

total = 0
width = 1
start_index = 0

while width * 2 <= len(line):
	part_counter = 0
	for i in range(width):
		if line[start_index + i] != line[start_index + width + i]:
			part_counter += 1
	total += part_counter

	width *= 2
	start_index += width

print(f"Total: {total}")
