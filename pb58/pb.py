import random

# Implementing Miller-Rabin primality test : n is an odd number | n < 4,759,123,141
def is_prime_Miller_Rabin(n):
	m = n - 1
	s = 0
	
	while m % 2 == 0:
		s += 1 # 2
		m /= 2 # 10

	d = (n - 1) // (2 ** s) # 5

	for a in [2, 7, 61]:
		if (a ** d) % n != 1:
			is_composite = True

			for r in range(0, s):

				if (a ** ((2 ** r) * d)) % n != -1:
					is_composite = False
					break

			if is_composite == True:
				return False

	return True

# Fermat primality test
def is_prime_Fermat(n): # !! Probabilistic !!
	k = 3
	m = n - 1

	for i in range(0, k):
		a = random.randint(1, m)

		if (a ** m) % n != 1:
			return False

	return True	

def solution():
	side_length = 2
	diagonals = [3, 5, 7, 9]
	nb_primes = 3
	nb_total = 5

	while nb_primes * 10 > nb_total:
		side_length += 2
		print (side_length + 1)
		diagonals = [diagonals[3] + side_length, diagonals[3] + 2 * side_length, diagonals[3] + 3 * side_length, diagonals[3] + 4 * side_length]

		if is_prime_Fermat(diagonals[0]) == True:
			nb_primes += 1
		if is_prime_Fermat(diagonals[1]) == True:
			nb_primes += 1
		if is_prime_Fermat(diagonals[2]) == True:
			nb_primes += 1

		nb_total += 4

	return side_length + 1

print solution()
