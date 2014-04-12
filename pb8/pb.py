file = open('number.txt', 'r')

string = file.readline()[0:-1]

file.close()

numbers = []

for number in string:
	numbers.append(int(number))

produit_max = 0

for index, number in enumerate(numbers):
	if index <= 995:
		produit = number*numbers[index + 1]*numbers[index + 2]*numbers[index + 3]*numbers[index + 4]

		if produit > produit_max:
			produit_max = produit
	else:
		break

print produit_max
