import math
import re

with open("test.txt") as f:
	numbers = list(map(int, re.findall(r'\d+', f.read())))
	total_time = -sum([-numbers[0], +numbers[1], *numbers[4:]])
	print(total_time // numbers[2])
