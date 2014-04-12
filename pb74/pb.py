mapping = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}

def f(x):
	global mapping
	result = 0

	for d in str(x):
		result += mapping[d]

	return result

def solution():
	t = [0] * 2177281
	result = 0
	i = 1

	while i <= 1000001:
		j = i

		while t[j] == 0:
			v = f(j)

			if v < 2177281:
				t[j] = v
				j = v
			else:
				break

		i += 1

	# Second part : Counting
	i = 1

	while i <= 100001:
		if t[i] != 0:
			s = set([i])
			j = t[i]

			while j not in s:
				s.add(j)
				j = t[j]
			
			if len(s) == 60:
				result += 1

		i += 1

	return result

print solution()
