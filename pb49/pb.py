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

def are_permutations(a, b, c):
	q = sorted(str(b))

	return (sorted(str(a)) == q) and (q == sorted(str(c)))

def solution():
	primes = primes_below(10000)
	primes = primes[168: len(primes)] # let's start from 4-digits primes
	primes_set = set(primes)

	for i, prime in enumerate(primes):
		for next_prime in primes[i + 1 : len(primes)]:
			test = 2 * next_prime - prime

			if test in primes:
				if are_permutations(prime, next_prime, test) and prime != 1487:
					return str(prime) + str(next_prime) + str(test)

print solution()
