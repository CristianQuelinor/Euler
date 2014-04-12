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

primes = primes_below(2000000)
somme = 0

for prime in primes:
	somme += prime

print somme
