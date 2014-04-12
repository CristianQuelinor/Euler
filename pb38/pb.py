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

max_pandigital = 0

for a in range(1, 98766):
	b = a
	i = 1

	while b < 10 ** 8:
		if b >= 10 ** 10:
			break
		
		else:
			i += 1
			b = concat_numbers(b, i * b)
			
	if is_pandigital(b) == True and max_pandigital < b:
		max_pandigital = b

print max_pandigital
