import random

def bank_account():
    bank_account == 100
    
def get_bet():
    bet = int(input("Enter a whole number for your bet:"))
    if bet < 0:
        return("This is an invalid amount. Your bet must be a positive integer!")
    if bet > 100:
        return("This is over your available amount.")
    return bet
    
    
def first_roll_result():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum
 

#option 1
#functio: first_roll_result
#purpose:get the result of the first roll
#arguments:roll - sum of the two dice rolled
#returns the result
#if roll is 7,11: return win
#if roll  is 2,3,12: return"lose"

    
def first_roll(dice_sum,point_roll):
    if dice_sum == 7 or dice_sum == 11:
        return("You win!")
    if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
        return("You lose")
    else:
        dice_sum == point_roll
        
        

def phase_three_bet(bank_account):
    p3_bet = input("Do you want to keep playing? Yes or No?")
    if p3_bet == "Yes":
        return("You have {} in your bank account.".format(get_bet))
    if p3_bet == "No":
        return("Thank you for playing.")
        bank_account = bank_account
        
def phase_three(dice_sum, point_roll):
    point_roll = first_roll_result()
    if dice_sum == 7:
        return("You lose")
    if dice_sum == point_roll:
        return("You win!")
    
def phase_winner(point_roll, bank_account):
    if dice_sum == point_roll or dice_sum == 7:
        return bet
         
    # return twice the amount of betted money to the winner
# if computer or dealer wins, give the money to the dealer
