import re
import math

with open("test.txt") as f:
	rida = f.readlines()[0].strip()

last_was_upper = False
pikkus = 0
praegune_algus = 0
pikima_algus = 0
pikim_pikkus = 0
for i, taht in enumerate(rida):
	if i == 0:
		last_was_upper = taht.isupper()
		continue

	# Then it's all good! 
	if taht.isupper() != last_was_upper:
		pikkus += 1
		if pikkus > pikim_pikkus:
			pikim_pikkus = pikkus
			pikima_algus = praegune_algus
		last_was_upper = taht.isupper()
	elif taht.isupper() == last_was_upper:
		praegune_algus = i
		pikkus = 0

print(pikima_algus, pikim_pikkus)
print(rida[pikima_algus:pikima_algus + pikim_pikkus + 1])
