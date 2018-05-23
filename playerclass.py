class Player():
	def __init__(self, name, money):
		self.name = name
		self.money = money

	def __str__(self):
		return f'{self.name}: {self.money}'

	def get_money(self):
		return self.money

	def get_name(self):
		return self.name

	def set_money(amount):
		self.money = amount

