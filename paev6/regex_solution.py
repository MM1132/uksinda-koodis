import re
from functools import reduce

with open("test.txt") as f:
	line = f.readline().strip()

mat = re.finditer(r'([a-z][A-Z])+|([A-Z][a-z])+', line)

longest_match = \
	reduce(lambda a, b: b if len(b.group()) > len(a.group()) else a, mat)

print(longest_match.group())
