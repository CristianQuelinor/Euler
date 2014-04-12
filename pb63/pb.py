def solution():
	nb = 0

	for n in range(1, 100):
		i = 1

		while len(str(i ** n)) < n:
			i += 1

		while len(str(i ** n)) == n:
			i += 1
			nb += 1

	return nb

print solution()
