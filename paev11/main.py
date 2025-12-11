with open("test.txt") as f:
	raw = f.read().strip()
	lines = [line.strip() for line in raw.split("\n")]

for i1 in range(len(lines)):
	for i2 in range(len(lines)):
		if i1 != i2 and lines[i1] == lines[i2]:
			lines[i1] = ""
			lines[i2] = ""

print(lines)

counter = len(lines) - lines.count("")

print(counter / 2)
