import math

with open("input.txt") as f:
	lines = f.readlines()

def solve(lines):
	result = 0
	numbers1 = lines[0].split(" ")
	numbers2 = lines[1].split(" ")

	for i in range(len(numbers1)):
		result += int(numbers1[i]) * int(numbers2[i])

	print(result)
	

if __name__ == '__main__':
	solve(lines)
