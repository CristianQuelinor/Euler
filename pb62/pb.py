def solution():
	cubes = [n * n * n for n in range(4642, 10000)]
	cubes_sorted = sorted([int(''.join(sorted(str(cube)))) for cube in cubes])

	(a, b, c, d, e, n) = (cubes_sorted[0], cubes_sorted[1], cubes_sorted[2], cubes_sorted[3], cubes_sorted[4], 5)

	while a != b or b != c or c != d or d != e:
		(a, b, c, d, e, n) = (b, c, d, e, cubes_sorted[n], n + 1)
		
	for cube in cubes:
		if int(''.join(sorted(str(cube)))) == a:
			return cube

print solution()
