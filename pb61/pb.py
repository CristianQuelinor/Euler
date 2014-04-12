def solution():
	# TRIANGLES
	triangles = []
	n = 1
	triangle = 1

	while triangle < 10000:
		if triangle > 999:
			triangles.append([n, triangle])
		n += 1
		triangle = n * (n + 1) / 2

	# SQUARES
	squares = []
	n = 1
	square = 1

	while square < 10000:
		if square > 999:
			squares.append([n, square])
		n += 1
		square = n * n

	# PENTAGONALS
	pentagonals = []
	n = 1
	pentagonal = 1

	while pentagonal < 10000:
		if pentagonal > 999:
			pentagonals.append([n, pentagonal])
		n += 1
		pentagonal = n * (3 * n - 1) / 2

	# HEXAGONALS
	hexagonals = []
	
	for i in range(0, len(triangles), 2):
		hexagonals.append([23 + i // 2, triangles[i][1]])
	print hexagonals

	# HEPTAGONALS
	heptagonals = []
	n = 1
	heptagonal = 1

	while heptagonal < 10000:
		if heptagonal > 999:
			heptagonals.append([n, heptagonal])
		n += 1
		heptagonal = n * (5 * n - 3) / 2

	# OCTOGONALS
	octogonals = []
	n = 1
	octogonal = 1

	while octogonal < 10000:
		if octogonal > 999:
			octogonals.append([n, octogonal])
		n += 1
		octogonal = n * (3 * n - 2)

print solution()
