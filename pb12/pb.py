# Facteurs premiers de n
def decomposition_facteurs_premiers(n):
	decomposition = []
	diviseur = 2
	i = -1
	nb_diviseurs = 1

	while n != 1:
		if n % diviseur == 0:
			n = n // diviseur

			if i == -1:
				decomposition = [[diviseur, 1]]
				i = 0
			elif decomposition[i][0] == diviseur:
				decomposition[i][1] += 1
			else:
				i += 1
				decomposition.append([diviseur, 1])
		else:
			diviseur += 1
	
	for facteur in decomposition:
		nb_diviseurs *= (facteur[1] + 1)

	return decomposition

# Nombre de diviseurs de n (y compris 1 et lui meme)
def nb_diviseurs(n):
	decomposition = decomposition_facteurs_premiers(n)
	nb_diviseurs = 1
	
	for facteur in decomposition:
		nb_diviseurs *= (facteur[1] + 1)

	return nb_diviseurs

# Nombre de diviseurs du triangle n (y compris 1 et lui meme)
def nb_diviseurs_triangle(n):
	(a, b) = (n/2, n + 1) if n % 2 == 0 else (n, (n + 1)/2)

	decomposition_a = decomposition_facteurs_premiers(a)
	decomposition_b = decomposition_facteurs_premiers(b)
	decomposition = decomposition_facteurs_premiers(a)

	# Fusion des decompositions

	for facteur_b in decomposition_b:
		index = 0
		exist = 0
		while index < len(decomposition_a):
			facteur_a = decomposition_a[index]
			if facteur_a[0] == facteur_b[0]:
				decomposition[index][1] += facteur_b[1]
				exist = 1
				break
			index += 1
		if exist == 0:
			decomposition.append(facteur_b)

	# Comptage

	nb_diviseurs = 1
	
	for facteur in decomposition:
		nb_diviseurs *= (facteur[1] + 1)

	return nb_diviseurs

# Calcul

n = 2
triangle = 3

while nb_diviseurs_triangle(n) < 500:
	n += 1
	triangle += n

print triangle
