import random

# Spill en omgang: Doble helt til du vinner
def omgang(bankroll):
	innsats = 1
	tap = random.random() < 0.5
	while tap and bankroll > innsats*2:
		# "tap": Dobler innsatsen:
		innsats *= 2
		tap = random.random() < 0.5

	if tap:
		print(f"Der gikk det drlig. Bankroll var {bankroll} og forrige innsats var {innsats}")

	return tap
	

bankroll = 1000
for i in range(1000): # Spill tusen ganger - tjener 1 kr per omgang
	tap = omgang(bankroll)
	if tap:
		print("Du tapte")
		break
	else:
		bankroll += 1
		# print("En omgang gikk bra. Bankroll er", bankroll)

if not tap:
	print(f"Gratulerer! Du har {bankroll} kr")
