mapping = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}

def f(x):
	global mapping
	result = 0

	for d in str(x):
		result += mapping[d]

	return result

def solution():
	

	return result

print solution()
