import re
import math

with open("input.txt") as f:
	lines = f.readlines()
	hinnangute_number = int(lines[0].strip())
	hotellide_number = int(lines[hinnangute_number + 1].strip())

	punktid = [line.strip().split(":") for line in lines[1: hinnangute_number + 1]]
	for p in punktid:
		p[1] = int(p[1].strip())
		p[0] = p[0].strip().lower()
		
	hinnangud = [line.strip().split(":") for line in lines[hinnangute_number + 2:]]
	for hinnang in hinnangud:
		hinnang[0] = int(hinnang[0].strip())
		hinnang[1] = hinnang[1].strip().lower()


# print(hinnangud)
# print(len(hinnangud))

# print(punktid)

counter = 0
for hinnang in hinnangud:
	uus_hinnang = 0
	# print("hotell:", h[0])
	kirjeldused = [i for i in hinnang[1].split(", ")]
	for k in kirjeldused:
		mitu = 0
		for p in punktid:
			if p[0] == k:
				uus_hinnang += p[1]
			# print(p[1], "sest:", p[0])
	if uus_hinnang > 10:
		counter += 1
	# print("hotelli", h[0], "hinnang on:", uus_hinnang)
	# print("counter: ", counter)
	# print()

print(counter)

# print(hinnangud)

# print(hinnangute_number)
# print(hotellide_number)
