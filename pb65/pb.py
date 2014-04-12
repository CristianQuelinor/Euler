def sum_digits(n):
	result = 0

	for d in str(n):
		result += int(d)

	return result

def solution():
	n_k_m_1 = 1
	n = 2
	
	for i in range(1, 100):
		a = 1 if (i % 3) != 2 else ((i - 2) / 3 + 1) * 2
		(n, n_k_m_1) = (a * n + n_k_m_1, n)

	return sum_digits(n)

print solution()
