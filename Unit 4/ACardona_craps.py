import random

    
def bet(bank_account, bet):
    while True:
        print("You have ${} in your bank account".format(bank_account))
        bet = int(input("Enter a whole number for your bet: $"))
        if bet < 0:
            print("This is an invalid amount. Your bet must be a positive integer!")
        elif bet > 100:
            print("This is over your available amount.")
        else:
            return bet
    
    
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    print("Total: {}".format(dice1 + dice2))
    return dice_sum
 

#option 1
#functio: first_roll_result
#purpose:get the result of the first roll
#arguments:roll - sum of the two dice rolled
#returns the result
#if roll is 7,11: return win
#if roll  is 2,3,12: return"lose"

    
def first_roll_result(dice_sum, bank_account):
    if dice_sum == 7 or dice_sum == 11:
        bank_account = bank_account + bet
        print("You win!")
        print("You have ${} in your bank account".format(bank_account)) 
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        bank_account = bank_account - bet
        print("You lose")
        return("You lose!")       
    else:
        return dice_sum
    print("You have ${} in your bank account".format(bank_account)) 
 # lines 34-42 is made to determine whether the number is a losing number or a winning number which is point roll.
 # point roll is the number that was rolled in the first round but it can't equal 7. Point roll is any winning number for the next round.
 
def point_roll_result(point_roll, dice_sum):
    if dice_sum == 7:
        return("You lose!")
    elif dice_sum != 7:
        return("You win!")
    
    
    
def second_roll_result(dice_sum,point_roll):
    if dice_sum == 7:
        print("You lose")
    if dice_sum == point_roll:
        print("You win")
    else:
        while (dice_sum != 7 and dice_sum != point_roll):
            dice_sum = roll2dice()
            if dice_sum == 7:
                print("You lose!")
                return "You lose!"
            elif dice_sum == point_roll:
                print("You won!")
                return "You won"
   
        


        
def craps():
    bank_account = 100
    bet(bank_account, bet)
    dice = roll2dice()
    first_result = first_roll_result(dice, bank_account)
    if first_result == "You win!":
        bank_account = bank_account + bet
        print("You win!")
        print("You have ${} in your bank account".format(bank_account)) 
    else:
        print("point roll")
    diceroll = roll2dice()
    point_roll_result = second_roll_result(dice,first_result)
    if point_roll_result == "You win!":
        print("You win!")
    if point_roll_result == "You lose!":
        bank_account = bank_account - bet
        print("You lose!")
        print("You have ${} in your bank account".format(bank_account)) 
    diceroll = roll2dice()
    point_roll_result = second_roll_result(dice,first_result)
    print ("_________________________________")
           
        
craps()
        
#def phase_three(dice_sum, point_roll):
#    point_roll = first_roll_result()
#    if dice_sum == 7:
#        return("You lose")
#    if dice_sum == point_roll:
#        return("You win!")
#    
#def phase_winner(point_roll, bank_account):
#    if dice_sum == point_roll or dice_sum == 7:
#        return 
         
    # return twice the amount of betted money to the winner
# if computer or dealer wins, give the money to the dealer
