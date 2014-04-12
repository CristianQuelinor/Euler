def factorial(n):
	if n <= 1:
		return 1

	else:
		return n * factorial(n - 1)

def C(k, n):
	return factorial(n) / (factorial(k) * factorial(n - k))

def solution():
	result = 0

	for n in range(1, 101):
		for k in range(0, 101):
			if C(k, n) >= 1000000:
				result += 1

	return result

print solution()
