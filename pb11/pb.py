def max_vertical_product(grid):
	max_product = 0

	for i in range(0, 17):
		for j in range(0, 20):
			product = grid[i][j]*grid[i + 1][j]*grid[i + 2][j]*grid[i + 3][j]

			if max_product < product:
				max_product = product

	return max_product

def max_horizontal_product(grid):
	max_product = 0

	for i in range(0, 20):
		for j in range(0, 17):
			product = grid[i][j]*grid[i][j + 1]*grid[i][j + 2]*grid[i][j + 3]

			if max_product < product:
				max_product = product

	return max_product

def max_diagonal_product(grid):
	max_product = 0

	for i in range(0, 17):
		for j in range(0, 17):
			product = grid[i][j]*grid[i + 1][j + 1]*grid[i + 2][j + 2]*grid[i + 3][j + 3]

			if max_product < product:
				max_product = product

	for i in range(0, 17):
		for j in range(19, 2, -1):
			product = grid[i][j]*grid[i + 1][j - 1]*grid[i + 2][j - 2]*grid[i + 3][j - 3]

			if max_product < product:
				max_product = product

	return max_product

def max_product(grid):
	max_product = max_vertical_product(grid)
	product = max_horizontal_product(grid)

	if product > max_product:
		max_product = product

	product = max_diagonal_product(grid)
	
	if product > max_product:
		max_product = product

	return max_product

# Actual computation
grid = [[0 for j in range(0, 20)] for i in range(0, 20)]

file = open('grid.txt', 'r')

for i, line in enumerate(file):
	line = line.split(' ')
	
	for j, number in enumerate(line):
		grid[i][j] = int(number)

print max_product(grid)
