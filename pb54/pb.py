t = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def is_royal_flush(cards):
	color = cards[0][1]
	values = set(['T', 'J', 'Q', 'K', 'A'])

	if cards[0][0] in values:
		values.remove(cards[0][0])
	else:
		return False

	for i in range(1, 5):
		if cards[i][1] != color: # Check color
			return False
		elif cards[i][0] in values: # Check value
			values.remove(cards[i][0])
		else:
			return False

	return True

def is_straight_flush(cards):
	global t
	color = cards[0][1]
	values = [t[cards[0][0]]]

	for i in range(1, 5):

		if cards[i][1] != color: # Check color
			return False
		else: # Add value
			values.append(t[cards[i][0]])

	values = sorted(values)

	for i in range(1, 4):
		if values[i] - values[i - 1] != 1:
			return False

	return True

def is_four_of_a_kind(cards):
	global t
	values = []

	for i in range(0, 5): # Add values
		values.append(t[cards[i][0]])

	values = sorted(values)

	return (values[0] == values[1] and values[1] == values[2] and values[2] == values[3]) or (values[1] == values[2] and values[2] == values[3] and values[3] == values[4])

def is_full_house(cards): # Assuming it is not a four of a kind
	values = set([])

	for i in range(0, 5): # Add values
		values.add(cards[i][0])

	return (len(values) == 2)

def is_flush(cards):
	return (cards[0][1] == cards[1][1]) and (cards[1][1] == cards[2][1]) and (cards[2][1] == cards[3][1]) and (cards[3][1] == cards[4][1])

def is_straight(cards):
	global t
	values = [t[cards[0][0]]]

	for i in range(1, 5):
		else: # Add value
			values.append(t[cards[i][0]])

	values = sorted(values)

	for i in range(1, 4):
		if values[i] - values[i - 1] != 1:
			return False

	return True

def is_three_of_a_kind(cards): # Assuming this is not a full house or a four of a kind
	values = []

	for i in range(0, 5): # Add values
		values.append(cards[i][0])

	return len(set(values)) == 3

def is_two_pairs(cards): # Assuming this is not a full house or a four of a kind or a three of a kind
	values = []

	for i in range(0, 5): # Add values
		values.append(cards[i][0])

	return len(set(values)) == 3

def is_one_pair(cards):
	values = []

	for i in range(0, 5): # Add values
		values.append(cards[i][0])

	return len(set(values)) == 4

def highest_card_player(cards1, cards2):

	return

def who_wins(hands):
	cards1 = hands[0].split(' ')
	cards2 = hands[1].split(' ')

	# Royal Flush

	if is_royal_flush(cards1) == True:
		if is_royal_flush(cards2) == False:
			return 1

	else:
		if is_royal_flush(cards2) == True:
			return 2

	# Straight Flush

	if is_straight_flush(cards1) == True:
		if is_straight_flush(cards2) == False:
			return 1

	else:
		if is_straight_flush(cards2) == True:
			return 2

	# Four of a kind

	if is_four_of_a_kind(cards1) == True:
		if is_four_of_a_kind(cards2) == False:
			return 1

	else:
		if is_four_of_a_kind(cards2) == True:
			return 2

	# Full House

	if is_full_house(cards1) == True:
		if is_full_house(cards2) == False:
			return 1

	else:
		if is_full_house(cards2) == True:
			return 2

	# Flush

	if is_flush(cards1) == True:
		if is_flush(cards2) == False:
			return 1

	else:
		if is_flush(cards2) == True:
			return 2

	# Straight

	if is_straight(cards1) == True:
		if is_straight(cards2) == False:
			return 1

	else:
		if is_straight(cards2) == True:
			return 2

	# Three of a kind

	if is_three_of_a_kind(cards1) == True:
		if is_three_of_a_kind(cards2) == False:
			return 1

	else:
		if is_three_of_a_kind(cards2) == True:
			return 2

	# Two pairs

	if is_two_pairs(cards1) == True:
		if is_two_pairs(cards2) == False:
			return 1

	else:
		if is_two_pairs(cards2) == True:
			return 2

	# One pair

	if is_one_pair(cards1) == True:
		if is_one_pair(cards2) == False:
			return 1

	else:
		if is_one_pair(cards2) == True:
			return 2

	# Highest card

	return highest_card_player(cards1, cards2)

def solution():
	wins = 0
	hands = []

	file = open('poker.txt', 'r')

	for line in file:
		hands.append([line[0:14], line[15:29]])

	file.close()

	for hand in hands:
		if who_wins(hand) == 1:
			wins += 1

	return wins

print is_flush(['5H', 'TC', 'CC', 'AC', 'AC'])
