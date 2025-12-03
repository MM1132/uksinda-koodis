import math

a = [10, 5, 8, 3, 6]
b = [1, 3, 1, 2, 1]
c = zip(a, b)

result = 0
for v in c:
	result += v[0] * v[1]

print(result)
