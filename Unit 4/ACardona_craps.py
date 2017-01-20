import random

def get_bet(bank_account):
    while True:
        print("You have ${} in your bank account.".format(bank_account))
        bet=int(input("How much would you like to bet?: $"))
        if bet < 0:
            print("Your bet must be a positive integer higher than $0")
        elif bet> bank_account:
            print("You only have ${} to bet, you can't bet anymore!".format(bank_account))
        else:
            return bet

def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} + {}".format(dice1,dice2))
    print("Dice roll total: {}".format(dice1+dice2))
    return dice_sum
    
    


def first_roll_result(dice_sum):
    if dice_sum == 7 or dice_sum == 11:
        return "You won!"
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return "You lose!"
        
    else:
        return dice_sum

        
def second_roll_result(dice_sum,point_roll):
    if dice_sum == 7:
        return("You lose!")
        
    elif dice_sum == point_roll:
        return("You won!")
        
    else:
        while(dice_sum != 7 and dice_sum != point_roll):
            dice_sum=roll2dice()
            if dice_sum == 7:
                return "You lose!"
            elif dice_sum == point_roll:
                return "You won!"
                 

#option 1
#functio: first_roll_result
#purpose:get the result of the first roll
#arguments:roll - sum of the two dice rolled
#returns the result
#if roll is 7,11: return win
#if roll  is 2,3,12: return"lose"

 
      
 # lines 34-42 is made to determine whether the number is a losing number or a winning number which is point roll.
 # point roll is the number that was rolled in the first round but it can't equal 7. Point roll is any winning number for the next round.
 
        


        

def craps():
    bank_account=100
    while  bank_account > 0:
        bet = get_bet(bank_account)
        dice = roll2dice()
        first_result = first_roll_result(dice)
        if first_result == "You won!":
            print("You won!")
            bank_account = bank_account+bet
        elif first_result == "You lose!":
            print ("You lose!")
            bank_account = bank_account-bet
        else:
            print("point roll")
            dice = roll2dice()
            point_roll_result = second_roll_result(dice,first_result)
            if point_roll_result == "You lose!":
                print("You lose!")
                bank_account= bank_account-bet
            if point_roll_result == "You won!":
                print("You won!")
                bank_account= bank_account+bet
            
            
        print("____________________________________")
    
         
        
        
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
