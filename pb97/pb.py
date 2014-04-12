def solution():
	result = 1

	for i in range(0, 7830457):
		result = (2 * result % 10000000000)

	return ((28433 * result + 1) % 10000000000)

print solution()
