with open("input.txt") as f:
	line = f.read().strip()

# Remove first because always the same
print(f"{1} {line[0]} -> {0}")
line = line[1:]

changes_list = [0] * 20

total = 0
length = 1
level = 2
while len(line) >= length:
	left_part = line[:length]
	line = line[length:]

	right_part = reversed(line[:length])
	line = line[length:]

	changes = sum(1 for a, b in zip(left_part, right_part) if a != b)

	changes_list[level - 1] = changes
	total += changes

	print(f"{level} {len(left_part)} -> {changes}")

	length *= 2
	level += 1

print(f"Left in line: {line}")

for l in range(20):
	print(f"Level {l + 1} changes: {changes_list[l]}")

print(f"Sum: {sum(changes_list)}")

print(f"Total: {total}")


