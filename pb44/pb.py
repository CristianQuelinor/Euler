import math

def abs(n):
	if n < 0:
		return -n
	else:
		return n

def is_pentagonal(n):
	inverse_n = (math.sqrt(24 * n + 1) + 1.) / 6.

	return inverse_n == int(inverse_n) # it must be an integer to return True


def solution():
	j = 0

	while True:
		j += 1
		p_j = j * (3 * j - 1) / 2

		for k in range(1, j):
			p_k = k * (3 * k - 1) / 2

			if is_pentagonal(p_j + p_k) == True and is_pentagonal(p_j - p_k) == True:
				return p_j - p_k

print solution()
