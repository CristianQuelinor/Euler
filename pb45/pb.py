import math

def is_pentagonal(n):
	inverse_n = (math.sqrt(24 * n + 1) + 1.) / 6.

	return inverse_n == int(inverse_n) # it must be an integer to return True

def solution():
	n = 143 + 1
	h_n = n * (2 * n - 1)

	while is_pentagonal(h_n) == False: # triangular --> hexagonal and h_n is already pentagonal
		n += 1
		h_n = n * (2 * n - 1)

	return h_n

print solution()
