with open("test.txt") as f:
	sisend = f.readlines()[0]
	puu = []
	puu.append(list(map(int, sisend.split(" "))))

def f(numbrid):
	uus_rida = []
	for i in range(0, len(numbrid), 2):
		if numbrid[i] == 1 or numbrid[i + 1] == 1:
			uus_rida.append(1)
		else:
			uus_rida.append(0)
		if numbrid[i] == 0 and numbrid[i + 1] == 1:
			# 2 means that there is a problem
			numbrid[i] = 2 
		if numbrid[i + 1] == 0 and numbrid[i] == 1:
			numbrid[i + 1] = 2
	return uus_rida

while len(puu[-1]) >= 2:
	puu.append(f(puu[-1]))

katkised_indeksid = []
indeks = 0
for i in range(len(puu) - 1, -1, -1):
	for j in range(len(puu[i])):
		print(f"{puu[i][j]} ", end="")
		if puu[i][j] == 2:
			katkised_indeksid.append(indeks)
		indeks += 1
	print()

print()
print(f"Vastus: {' '.join(map(str, katkised_indeksid))}")
