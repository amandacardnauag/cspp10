import random
 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print dice_sum
    return dice_sum
    
    # generate a random number from 1 to 6
   
    # generate another random number from 1 to 6
   
    # get the sum of the two rolls
   
    # print the sum
   
    # return the sum
 
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    bank_account = 100
    bet = input(int("How much would you like to bet?"))
    while bet <= bank_account:
        print("Your bet is {}".format(bet))
    else:
        print("This is over your available amount.")
    
    
    
    # ask the player how much they want to bet
   
    # if player's bet is more than they have
    #   available in bank, then get new bet
   
    # if player's bet is valid, then return
    #   the bet
 
# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    if dice_sum > 7:
        return "over7"
    if dice_sum < 7:
        return "over7"
    if dice_sum == 7:
        return "equal7"
    # if the sum is over 7, return "over7"
   
    # if the sum is under 7, return "under7"
   
    # if the sum is 7, return "equal7"
 
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range(choice):
    print("Over7 means you want to roll 8-12. If won, winner recieves 1:1 payout")
    print("Under7 means you want to roll 2-6. If won, winner recieves 1:1 payout")
    print("Equal7 means you want to roll 7.If won, winner recieves 4:1 payout")
    choice = input("Choose one: over7, under7, equal7:")
    return choice
    # present user with choices "over7", "under7",
    #   or "equal7"
   
    # return their choice
def overunder7():
    #initialize the player's bank
    bank = 100
    #loop as long as the player has SOME amount of money
    while bank > 0:
        #ask for a bet and save it
        bet = get_bet(bank)
        #ask for the range and save it
        user_range = choose_range()
        #roll 2 dice and save it
        dice = roll2dice()
        #figure out the range of the dice and save it
        round_range = get_range(dice)
        #check to see if the user won or lost
        #update their bank accordingly
         
        round_range = get_range(dice)
        if user_range == round_range: #user won
            print "You win"
        if user_range == "equal7":
            print "You win"
            bank = bank + 4 * bet
        else: #user lost
            print "You lose"
            bank = bank - bet
        print("Your balance is ${}".format(bank))
        
        new_round = input("Do you want to continue? [y|n]")
        if new_round != "y":
            break