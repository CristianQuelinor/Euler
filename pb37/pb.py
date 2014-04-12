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

def is_truncatable(n, primes):
	pow = 10;

	while pow < n:
		if (n % pow in primes) == False or (int(n / pow) in primes) == False:
			return False;

		pow *= 10;
	return True

# Actual computation
cardinal = 0
somme = 0
primes = primes_below(1000000)
primes_to_test = primes[4:]

for prime in primes_to_test:
	if is_truncatable(prime, primes) == True:
		somme += prime
		cardinal += 1

	if cardinal == 11:
		break

print somme
