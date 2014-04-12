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

def check_conjecture(n):
	global primes

	i = 1
	test = n - i  * i

	while test > 0:
		if test in primes:
			return True
		else:
			i += 1
			test = n - i  * i

	return False

def generate_composites(primes):
	composites = []
	
	for i in range(0, len(primes)):
		for j in range(i, len(primes)):
			composites.append(primes[i] * primes[j])

	return sorted(composites)

def solution():
	primes = primes_below(1000)
	primes.remove(2)
	composites = generate_composites(primes)
	primes_set = set(primes_below(10000))
	
	for n in composites:
		conjecture = False
		i = 1
		test = n - 2 * i * i

		while test > 0:
			if test in primes_set:
				conjecture = True
				break
			else:
				i += 1
				test = n - 2 * i * i

		if conjecture == False:
			return n

print solution()
			
			

