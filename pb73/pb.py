import fractions

def is_proper(n, d):
	return fractions.gcd(n, d) == 1

def solution():
	result = 0

	for d in range(2, 12001):
		for n in range(d / 3 + 1, (d - 1) / 2 + 1):
			if is_proper(n, d):
				result += 1

	return result

print solution()
