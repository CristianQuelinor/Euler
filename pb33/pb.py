import fractions

m, n = 1, 1

# (a * 10 + c) / (c * 10 + b) < 1 :
for a in range (1, 10):
	for b in range(a + 1, 10):
		for c in range(b + 1, 10):	
			if (10 * a + c) * b == (10 * c + b) * a:
				m *= a
				n *= b

n = n / fractions.gcd(m, n)
print n
