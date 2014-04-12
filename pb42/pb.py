weights = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, '\n': 0}

file = open('words.txt', 'r')

line = file.readline()

file.close()

words = line.split(',')
triangle_numbers = [1]
nb_triangle_words = 0

for i in range(2, 100):
	triangle_numbers.append(triangle_numbers[i - 2] + i)

for word in words:
	score = 0

	for letter in word:
		score += weights[letter]

	if score in triangle_numbers:
		nb_triangle_words += 1

print nb_triangle_words
