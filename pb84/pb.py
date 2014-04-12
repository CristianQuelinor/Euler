import random

def take_CC(position):
	r = random.randint(0,15)
	
	if r == 0: # Case: Go to GO
		return 40 - position
	elif r == 1: # Case: Go to JAIL
		return (10 - position) % 40
	else: # Case: Don't move
		return 0

def take_CH(position):
	r = random.randint(0, 15)
	
	if r == 0: # Case: Go to GO
		return 40 - position
	elif r == 1: # Case: Go to JAIL
		return (10 - position) % 40
	elif r == 2: # Case: Go to C1
		return (11 - position) % 40
	elif r == 3: # Case: Go to E3
		return (24 - position) % 40
	elif r == 4: # Case: Go to H2
		return (39 - position) % 40
	elif r == 5: # Case: Go to R1
		return (5 - position) % 40
	elif r == 6 or r == 7: # Case: Go to next R
		d = position % 10

		if d < 5:
			return 5 - d
		else:
			return 15 - d

	elif r == 8: # Case: Go to next U
		if position < 12:
			return 12 - position
		elif position < 28:
			return 28 - position
		else:
			return 52 - position

	elif r == 9: # Case: Go back 3 squares
		return (position - 3) % 40
	else: # Case: Don't move
		return 0

def roll_dices():
	return (random.randint(1, 4),random.randint(1, 4))

def max_three_indexes(input_list):
	# input_list[a] > input_list[b] > input_list[c]

	if input_list[0] > input_list[1]:
		if input_list[2] > input_list[0]:
			(a, b, c) = (2, 0, 1)
		elif input_list[2] > input_list[1]:
			(a, b, c) = (0, 2, 1)
		else:
			(a, b, c) = (0, 1, 2)
	else:
		if input_list[2] > input_list[1]:
			(a, b, c) = (2, 1, 0)
		elif input_list[2] > input_list[0]:
			(a, b, c) = (1, 2, 0)
		else:
			(a, b, c) = (1, 0, 2)
	
	for i, value in enumerate(input_list[3:len(input_list)]):
		if input_list[i] > input_list[c]:
			c = i

			if input_list[c] > input_list[b]:
				tmp = c
				c = b
				b = tmp
			if input_list[b] > input_list[a]:
				tmp = a
				a = b
				b = tmp

	return (a, b, c)

def solution():
	squares_occurences = [0] * 40
	squares_occurences[0] = 1
	position = 0
	consecutive_doubles = 0

	for i in range(0, 100000):
		(d1, d2) = roll_dices()

		# Managing doubles
		if d1 == d2:
			consecutive_doubles += 1

			if consecutive_doubles == 3:
				position = 10 # Go to JAIL
				squares_occurences[10] += 1
				continue
		else:
			consecutive_doubles = 0

		position += ((d1 + d2) % 40)

		# Managing CH squares:
		if position == 7 or position == 22 or position == 36:
			position += take_CH(position)
		# Managing CC squares:
		elif position == 2 or position == 17 or position == 33:
			position += take_CC(position)
		# Managing G2JAIL square:
		elif position == 30:
			position = 10

		position %= 40
		squares_occurences[position] += 1

	(a, b, c) = max_three_indexes(squares_occurences)
	return str(a) + str(b) + str(c)

print solution()
