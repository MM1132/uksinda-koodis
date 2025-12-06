import re

with open("test.txt") as f:
	lines = f.readlines()

pattern = re.compile(r'(?:(?<=^)|(?<=[0 ]))0(?=[0 ]|$)')

positions = []
for line_i in range(len(lines)):
	for v in pattern.finditer(lines[line_i]):
		x = v.span()[0]
		if x < 3:
			x += 1
		if x > 8:
			x -= 1
		positions.append((line_i + 1, x))
print(positions)
