from playerclass import *
from blackjackfunc import *

while True:
	game = True #whether a player bankrupts

	print('Welcome to blackjack game')

	fund = enter_int('Please enter starting fund: ')
	print(f'\nYour starting bank account is ${fund}\n')


	humanname = input('Please type your name: ')
	p0 = Player(humanname, fund)
	p1 = Player('Computer', fund)

	p0.set_money(fund)
	p1.set_money(fund)


	while game:
		print('Game begins!')
		deck = init_deck()


		#enter bet amount
		while True: 
			bet = enter_int('Please enter your bet amount: ')
			if bet < p0.get_money():
				break

			else:
				print(f'Your balance is ${p0.get_money()}')

		p0.reset_cards()
		p1.reset_cards()
		p0.new_card(draw(deck))
		p1.new_card(draw(deck))
		diff0 = p0.new_card(draw(deck))
		diff1 = p1.new_card(draw(deck))
		print(p0)
		print(p1)
		
		

		hit = 'hit' == input('Do you want to hit [hit] or stay [stay]? ').lower()

		#player choose hit
		while hit:
			diff0 = p0.new_card(draw(deck))
			print(p0)
			if diff0 < 0:
				original_money = p0.get_money()
				p0.set_money(original_money - bet)
				print(f'You Lose! your current balance is: ${p0.get_money()}')
				break

			hit = 'hit' == input('Do you want to hit [hit] or stay [stay]? ').lower()

		if p0.get_money() <= 0:
			print('You are Bankrupt! \nGame will exit now!')
			game = False
			break


		while diff1 > diff0 >0:
			diff1 = p1.new_card(draw(deck))
			print(p1)

		if diff1 > 0 and diff0 > 0: #computer is closer to 21
			original_money = p0.get_money()
			p0.set_money(original_money - bet)
			print(f'You Lose! your current balance is: ${p0.get_money()}')
			if p0.get_money() <= 0:
				print('You are Bankrupt! \nGame will exit now!')
				game = False
				break

		elif diff0 > 0: #computer goes over 21
			original_money = p0.get_money()
			p0.set_money(original_money + bet)
			print(f'You Win! your current balance is: ${p0.get_money()}')

		if 'y' != input('Do you still want to play? [Y/N]').lower():
			game = False

	print(f'You walk away with ${p0.get_money()}')
	break



