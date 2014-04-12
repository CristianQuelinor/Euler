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

def solution():
	primes = primes_below(10 ** 6)
	primes_set = set(primes)
	sums = primes
	max_primes = 0
	delta_max = 0

	for i in range(1, len(primes)):
		sums[i] += sums[i - 1]

	for i in range(max_primes, len(sums) - 1):
		for j in range(i - 1 - max_primes, -1, -1):
			delta = sums[i] - sums[j]

			if delta > 10 ** 6:
				break

			if delta in primes_set:
				max_primes = i - j + 1
				delta_max = delta

	return delta_max

print solution()
