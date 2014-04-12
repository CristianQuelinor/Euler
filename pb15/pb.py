import math

def nCk(n, k):
	return math.factorial(n) / math.factorial(k) / math.factorial(n - k)

def nb_paths(taille):
	return nCk(2*taille, taille)

print nb_paths(20)
