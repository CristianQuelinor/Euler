def abs(n):
	if n > 0:
		return n
	else:
		return -n

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

def nb_consecutive_primes(a, b):
	global big_primes

	nb = 0

	for n in range(0, b):
		if abs((n * (n + a) + b)) in big_primes:
			nb += 1

		else:
			break

	return nb

#############

big_primes = primes_below(2001001)
small_primes = big_primes[1:168] # primes < 1000
big_primes = set(big_primes)
product_ab_max = 0
m_max = 0

for a in range(-999, 1001, 2):

	# b is an even prime number
	
	a -= 1

	# b = 2
	m = nb_consecutive_primes(a, 2)

	if m > m_max:
		m_max = m
		product_ab_max = a * 2
		
	# b = -2
	
	m = nb_consecutive_primes(a, -2)

	if m > m_max:
		m_max = m
		product_ab_max = -a * 2

	# b is an odd prime number
	
	a += 1

	for b in small_primes:
		
		# b > 0
		
		m = nb_consecutive_primes(a, b)

		if m > m_max:
			m_max = m
			product_ab_max = a * b
		
		# b < 0
		
		m = nb_consecutive_primes(a, -b)

		if m > m_max:
			m_max = m
			product_ab_max = -a * b

print product_ab_max
