def reverse(n):
	return int(str(n)[::-1])

def is_palindromic(n):
	return n == reverse(n)

def is_lychrel(n):
	for i in range(0, 50):
		m = n + reverse(n)

		if is_palindromic(m):
			return False

		else:
			n = m

	return True

def solution():
	nb = 0

	for i in range(1, 10000):
		if is_lychrel(i):
			nb += 1

	return nb

print solution()
