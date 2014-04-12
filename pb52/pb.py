def has_same_digits(a, b, c, d, e, f):
	return sorted(str(a)) == sorted(str(b)) and sorted(str(b)) == sorted(str(c)) and sorted(str(c)) == sorted(str(d)) and sorted(str(d)) == sorted(str(e)) and sorted(str(e)) == sorted(str(f))

def solution():
	(a, b, c, d, e, f) = (1, 2, 3, 4, 5, 6)

	while has_same_digits(a, b, c, d, e, f) == False:
		(a, b, c, d, e, f) = (a + 1, b + 2, c + 3, d + 4, e + 5, f + 6)
	return a

print solution()
