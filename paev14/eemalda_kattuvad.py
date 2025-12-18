with open("input.txt") as f:
	line = f.read().strip()
	numbers = eval(line)

for i in range(len(numbers) - 1):
	for j in range(i + 1, len(numbers)):
		if numbers[i] == numbers[j]:
			print(f"numbers at {i} and {j} are the same. Number is {numbers[i]}")
