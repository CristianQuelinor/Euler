def concat_numbers(a, b):
	c = b

	while c > 0:
		a *= 10
		c /= 10

	return a + b

def is_pandigital(n):
	if len(str(n)) != 9:
		return False
	
	else:
		n = sorted(str(n))

		for i, j in enumerate(n):
			if str(i + 1) != j:
				return False

		return True

pandigitals = set()

for a in range(1, 9876):
	for b in range(a, 10000 // a):
		m = a * b

		if is_pandigital(concat_numbers(concat_numbers(a, b), m)) == True:
			pandigitals.add(m)

print sum(pandigitals)
