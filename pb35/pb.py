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

primes = set(primes_below(1000000))
count = 0

for prime in primes:
	is_circular = True
	n = prime
	l = 0

	while 10 ** l < n:
		l += 1

	for i in range(0, l):
		f = int(n / 10 ** (l - 1))
		n = n * 10 + f * (1 - 10 ** l)

		if n not in primes:
			is_circular = False
			break

	if is_circular == True:
		count += 1

print count
