# list(map(lambda x: x * 2))

import math

with open("test.txt") as f:
	lines = f.readlines()

	numbrid_esimene_rida = lines[0].split(" ")

	aega_lennuni = int(numbrid_esimene_rida[0])
	minuti_kaugusel_terminal = int(numbrid_esimene_rida[1])
	uhe_snaki_soomine = int(numbrid_esimene_rida[2])

	jarjekorras_inimesi = int(lines[1])

	inimeste_ajad_kokku = sum(list(map(int, lines[2].split(" "))))

aega = aega_lennuni - minuti_kaugusel_terminal
aega -= inimeste_ajad_kokku

print("aega_lennuni", aega_lennuni)
print("minuti_kaugusel_terminal", minuti_kaugusel_terminal)
print("inimeste_ajad_kokku", inimeste_ajad_kokku)
print("aega", aega)


print(aega / uhe_snaki_soomine)
