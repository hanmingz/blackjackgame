def init_deck():
	deck = []
	for i in range(2, 11):
		for j in range(1, 5):
			deck.append(i)

	for i in range(1, 13):
		deck.append(10)

	for i in range(1, 5):
		deck.append(111)

	return deck
