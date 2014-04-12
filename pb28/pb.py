# half_size : 1
somme, size, i, a, b, c, d = 1, 1, 2, 1, 1, 1, 1

while size < 1001:
	(a, b, c, d) = (d + i, d + 2*i, d + 3*i, d + 4*i)
	i += 2
	size += 2
	somme += (a + b + c + d)

print somme
