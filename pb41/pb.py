def is_pandigital(n, order):
	if len(str(n)) != order:
		return False
	
	else:
		n = sorted(str(n))

		for i, j in enumerate(n):
			if str(i + 1) != j:
				return False

		return True

# Implementing Eratosthene
def primes_below(n):
	primes = [True] * (n + 1)
	primes [0], primes[1] = False, False

	i = 2

	while i <= n:
		j = i*2
		
		while j <= n:
			primes[j] = False
			j += i
		
		i += 1

		while i <= n and primes[i] == False:
			i += 1

	result = []

	for number, is_prime in enumerate(primes):
		if is_prime == True:
			result.append(number)

	return result

primes = primes_below(7654322) # all n-pandigital numbers are multiples of 3, except for n = 4 or 7
max_prime = 0

for prime in primes:
	if is_pandigital(prime, len(str(prime))) == True:
		max_prime = prime

print max_prime
