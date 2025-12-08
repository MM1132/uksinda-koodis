with open("input.txt") as f:
	file = f.read()
	first_number = int(file.split("\n")[0])

for v in [line.split(": ") for line in file.split("\n")[1:first_number + 1]]:
	file = file.replace(v[0], v[1])

total = 0
for v in [line.split(": ")[1] for line in file.split("\n")[first_number + 2:]]:
	if sum(map(int, v.split(", "))) > 10:
		total += 1

print(total)
