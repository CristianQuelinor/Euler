import itertools

all_permutations = list(itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))

values = []

for permutation in all_permutations:
	values.append(int(''.join(permutation)))

print values[999999]
