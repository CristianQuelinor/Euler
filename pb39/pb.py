max = 0
p_max = 0

for p in range(1, 1001):
	nb_solutions = 0
	limit = int(p / 3)

	for a in range(1, limit):
		for b in range(a + 1, p - 2*a):
			if a*a + b*b == (p - a - b)**2:
				nb_solutions += 1

	if nb_solutions > max:
		p_max = p
		max = nb_solutions

print p_max
