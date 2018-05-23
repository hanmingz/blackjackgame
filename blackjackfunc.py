import random
from playerclass import *

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

def draw(deck):
	index = random.randint(0, len(deck)-1)
	return deck.pop(index)

def enter_int(string):
	while True:
		try:
			num = int(input(string))

		except:
			print('Not an integer, please enter again')

		else:
			break

	return num

