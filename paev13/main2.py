with open("input.txt") as f:
	rida = f.read().strip()

rida = rida[1:]

muudatusi_kokku = 0
pikkus = 1
while len(rida) >= pikkus:
	vasak = rida[:pikkus]
	rida = rida[pikkus:]

	parem = list(reversed(rida[:pikkus]))
	rida = rida[pikkus:]

	for i in range(len(vasak)):
		if vasak[i] != parem[i]:
			muudatusi_kokku += 1

	pikkus *= 2

print(f"Kokku: {muudatusi_kokku}")
