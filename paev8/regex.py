import re

with open("input.txt") as f:
	lines = f.read().strip().split("\n")
	rotated_lines = ["".join(line) for line in list(zip(*lines))]
	lines += rotated_lines

line = " ".join(lines)

re_match = re.finditer(r'\w+', line)

longest = max([len(m.group()) for m in re_match])

print(longest)
