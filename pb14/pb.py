def length_c(n):
	somme = 0

	while n != 4:
		if n % 2 == 0:
			somme += 1
			n /= 2
		else:
			somme += 2
			n = (3*n + 1)/2

	return (somme + 3)

number_max = 4
length_max = 3

for number in range(4, 1000000):
	length = length_c(number)

	if length_max < length:
		number_max = number
		length_max = length

print(str(number_max) + " with length of " + str(length_max))
