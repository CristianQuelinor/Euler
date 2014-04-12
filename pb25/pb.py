a, b, term = 1, 1, 2

while len(str(b)) < 1000:
	(a, b, term) = (b, a + b, term + 1)

print term
