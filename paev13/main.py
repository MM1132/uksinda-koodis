with open("test.txt") as f:
	line = [int(n) for n in f.read().strip()]

line = line[1:]

print(f"Line: {line}")

counter = 0
length = 2
tase = 1
while len(line) >= length:
	tase += 1
	part = line[:length]
	line = line[length:]
	length *= 2
	print(f"Tase: {tase}")
	print(f"Part: {part}")

	left_part = part[:len(part) // 2]
	right_part = part[len(part) // 2:]

	print(f"Part <-: {"".join(map(str, left_part))}")
	print(f"Part ->: {"".join(map(str, right_part))}")
	difference_count = 0
	for i in range(len(left_part)):
		if left_part[i] != right_part[i]:
			difference_count += 1
			# print(f"{left_part[i]} and {right_part[i]} are not the same, thus incremented by 1")
	print(f"{difference_count} differences found in level {tase}")
	counter += difference_count
	print()

print(f"Left in line: {line}")

print(f"Counter: {counter}")

# 262142
