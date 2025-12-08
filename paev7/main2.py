def is_digit(n):
	try:
		int(n)
		return True
	except ValueError:
		return  False

with open("input.txt") as f:
	lines = f.readlines()

punktid = filter(lambda line: len(line.strip().split(": ")) == 2 and is_digit(line.strip().split(": ")[1]), lines)
punktid = [[rida.strip().split(": ")[0], int(rida.strip().split(": ")[1])] for rida in punktid]

hinnangud = filter(lambda line: len(line.strip().split(": ")) == 2 and is_digit(line.strip().split(": ")[0]), lines)
hinnangud = [rida.strip().split(": ")[1].strip().split(", ") for rida in hinnangud]

print(hinnangud)

counter = 0
for h in hinnangud:
	summa = 0
	for v in h:
		for p in punktid:
			if p[0] == v:
				summa += p[1]
	if summa > 10:
		counter += 1

print(counter)
