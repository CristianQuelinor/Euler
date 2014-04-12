modulo = 10**10
somme = 0

for i in range(1, 1001):
	somme += (i**i % modulo)

somme %= modulo
print somme
