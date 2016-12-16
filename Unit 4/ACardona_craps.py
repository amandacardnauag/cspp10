import random

    
def get_bet(bank_account):
    while True:
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

    
def first_roll_result(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        print("You win!")
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print("You lose")
    else:
        return dice_sum
    
def second_roll_result(dice_sum,point_roll):
    if dice_sum == 7 or dice_sum == point_roll:
        print("You won!")
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        print("You lose!")
    else:
        print("TRY AGAIN")
    return(second_roll_result)

def point_round(roll,point_roll):
    while (roll != 7 and roll != point_roll):
        print(roll2dice)
    return(second_roll_result(dice_sum,point_roll))                                                                                                                                                                                                                                                                                                                                                                                                                                                        ))
        
        
def craps():
    bank_account = 100
    get_bet(bank_account)
    dice = roll2dice
    first_result = first_roll_result(dice)
    if first_result == "You won!":
        print("You won!")
    elif first_result == "You lose!":
        print("You lose!")
    else:
        print("point roll")
        dice = roll2dice()
        point_roll_result = second_roll_result(dice,first_result)
    return(craps())
        
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
