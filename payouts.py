import math

print("Poker payouts made simple.")

players = int(input("How many players? "))

buyin = int(input("What was buy in ?: $"))
num_rebuys = int(input("How many rebuys? "))
num_addons = int(input("How many players added on? "))

add_on = 10

pot = buyin * (players + num_rebuys)

print('Total pot: $' + str(pot) + ".00")

#if players <= 4:
	#print('There are ' + str(players) + ' players.')

def calculate_payouts():
	if players <= 4:
		first = ${:,.2f}'.format(pot)
		return "First place pays: " + str(first)
	elif players <= 8:
		first = '${:,.2f}'.format(pot * .70)
		second = '${:,.2f}'.format(pot * .30)
		return "First place pays: " + str(first) + "\nSecond place pays: " + str(second)
	else:
		first = '${:,.2f}'.format(pot * .50)
		second = '${:,.2f}'.format(pot * .30)
		third = '${:,.2f}'.format(pot * .20)
		return "First place pays: $" + str(first) + "\nSecond place pays: " + str(second) + "\nThird place pays: " + str(third)

		
print(calculate_payouts())