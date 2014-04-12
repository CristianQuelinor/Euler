file = open('cipher1.txt', 'r')

message = file.readline().split(',')
message[len(message) - 1] = int(message[len(message) - 1])

file.close()

for n, m in enumerate(message):
	message[n] = int(m)

def analysis(message):
	maxsize = 0

	for j in message:
		if j > maxsize:
			maxsize = j
	
	a_message = []
	key = [0, 0, 0]

	for i in range(0, maxsize + 1):
		a_message.append([0, 0, 0])

	for i in range(0, len(a_message)):
		j = i % 3
		a_message[message[i]][j] += 1

		if a_message[message[i]][j] > a_message[key[j]][j]:
			key[j] = message[i]

	key[0] = key[0] ^ 101 # e
	key[1] = key[1] ^ 32 # space
	key[2] = key[2] ^ 32 # space
 
	return key

def solution():
	key = analysis(message)
	somme = 0

	for i, j in enumerate(message):
		somme += (key[(i % 3)] ^ j)

	return somme

print solution()
