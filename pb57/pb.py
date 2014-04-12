def number_of_digits(n):
	return len(str(n))

def solution():
	n = 1
	d = 1
	result = 0

	for i in range(1, 1001):
		(n, d) = (n + 2 * d, n + d)

		if number_of_digits(n) > number_of_digits(d):
			result += 1

	return result

print solution()
	
