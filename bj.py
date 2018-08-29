import random

stay = False

dealer = [random.randint(1,10),random.randint(1,10)]
player = [random.randint(1,10),random.randint(1,10)] 

if sum(dealer) <= 11:
	if dealer[0] == 1 and dealer[1] == 1:
		dealer[0] = 11
	elif dealer[0] == 1:
		dealer[0] = 11
	elif dealer[1] == 1:
		dealer[1] = 11
		
if sum(player) <= 11:
	if player[0] == 1 and player[1] == 1:
		player[0] = 11
	elif player[0] == 1:
		player[0] = 11
	elif player[1] == 1:
		player[1] = 11
		


def player_game():
    global stay
    print("Your hand: %s" % player ,"Score: %s" % sum(player))
    print("Dealer hand: %s" % dealer ,"Score: %s" % sum(dealer))
    hit = raw_input("Hit or Stay? ")
    if hit == "hit":
		player.append(random.randint(1,10))
		if sum(player) <= 11 and player[2] == 1:
			player[2] = 11
    elif hit == "stay":
        stay = True
        return stay
    else:
        print ("I'm sorry. you need to input 'Hit or Stay'.")
        
    
        
while 1:
	player_game()
	p_total = sum(player)
	dealer_bust = False
	if p_total > 21:
		print ("Hand: %s" % player)
		print ("You busted with a score of: %s" % p_total)
		break
	elif sum(dealer) == 21:
		print ("Dealer got 21! %s" % dealer)
		print ("You lose!")
		break
	if stay == True:
		print ("You stayed.")
		while sum(dealer) < 17:
			dealer.append(random.randint(1,10))
			if sum(dealer) <= 11 and dealer[2] == 1:
				dealer[2] = 11
			print (sum(dealer))
			if sum(dealer) == 21:
				break
			elif sum(dealer) > 21:
				dealer_bust = True
				break
		print ("Your hand: %s" % p_total)
		print ("Dealer hand: %s" % sum(dealer))
		if p_total > sum(dealer):
			print ("You Win!")
		elif dealer_bust == True:
			print ("You Win!")
		else:
			print ("You Lose!")
		break