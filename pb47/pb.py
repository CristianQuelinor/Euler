import math

# Implementing Eratosthene
def primes_below(n):
	primes = [True] * (n + 1)
	primes[0], primes[1] = False, False

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

def has_4_prime_factors(n, primes):
	nb = 0
	i = 0
	m = n
	
	for prime in primes:
		if prime ** 2 > n: # There's only one prime factor left
			if nb == 3:
				return True
			else:
				return False

		if m % prime == 0: # Counting another prime factor
			nb += 1

			if nb > 4:
				return False

		while m % prime == 0:
			m = (m / prime)

			if m == 1:
				return nb == 4

def solution():
	primes = primes_below(200000)
	n = 644
	(a, b, c, d) = (False, False, False, False)

	while a == False or b == False or c == False or d == False:
		n += 1
		(a, b, c, d) = (b, c, d, has_4_prime_factors(n, primes))

	return (n - 3)

print solution()
