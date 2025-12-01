import math

def solve():
	with open("input.txt") as f:
		line = f.readlines()[0]

	# Convert to numbers
	# lines = list(map(int, lines))

	started = False
	counter = 0
	for v in line:
		if v == "*" and started == False:
			started = True
			counter += 1
		elif v == "." and started == True:
			started = False

	print(counter)

if __name__ == "__main__":
	solve()
