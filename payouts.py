import math

print("\n\nPoker payout calculator.\n")

while True:
	try:
		players = input("How many players? ")
		players = int(players)
		break
	except ValueError:
		continue

while True:
	try:
		buyin = input("What is the buyin ? $")
		buyin = int(buyin)
		break
	except ValueError:
		continue
while True:
    try:
        add_on = input("How much to add on? $")
        add_on = int(add_on)
        break
    except ValueError:
        continue

while True:
	try:
		rebuys = input("How many rebuys? ")
		rebuys = int(rebuys)
		break
	except ValueError:
		continue
while True:
	try:
		addons = input("How many players added on? ")
		addons = int(addons)
		break
	except ValueError:
		continue



pot = buyin * (players + rebuys)

print('\n\nTotal pot: $' + str(pot) + ".00")


def calculate_payouts():
	if players <= 4:
		first = '${:,.2f}'.format(pot)
		return "\n\nFirst place pays: " + str(first)
	elif players <= 8:
		first = '${:,.2f}'.format(pot * .70)
		second = '${:,.2f}'.format(pot * .30)
		return "\nFirst place pays: " + str(first) + "\nSecond place pays: " + str(second)
	else:
		first = '${:,.2f}'.format(pot * .50)
		second = '${:,.2f}'.format(pot * .30)
		third = '${:,.2f}'.format(pot * .20)
		return "\nFirst place pays: " + str(first) + "\nSecond place pays: " + str(second) + "\nThird place pays: " + str(third)

def bounty_reward():
    bounty = '${:,.2f}'.format(rebuys * add_on)
    return "The bounty reward is: " + bounty

print(calculate_payouts())
print(bounty_reward())