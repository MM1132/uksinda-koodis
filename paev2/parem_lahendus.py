import math

with open("input.txt") as f:
	numbers1 = list(map(int, f.readline().split(" ")))
	numbers2 = list(map(int, f.readline().split(" ")))

together = zip(numbers1, numbers2)
result = sum([v[0] * v[1] for v in together])
print(result)
