class Player():
	def __init__(self, name, money):
		self.name = name
		self.money = money
		self.cards = []


	def __str__(self):
		return f'{self.name} cards: {self.cards}'

	def reset_cards(self):
		self.cards = []

	def get_money(self):
		return self.money

	def get_name(self):
		return self.name

	def get_cards(self):
		return self.cards

	def set_money(self, amount):
		self.money = amount

	def new_card(self, num):
		if num != 111:
			self.cards.append(num)

		else:
			if sum(self.cards) <= 10:
				self.cards.append(11)

			else:
				self.cards.append(1)

		return 21 - sum(self.cards)


