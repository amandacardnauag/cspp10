import random

#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    move = input("rock, paper or scissors:")
    return move
     

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    randy = random.randint(1,3)
    if randy == 1:
        return ("rock")
    elif randy == 2:
        return ("paper")
    elif randy == 3:
        return ("scissors")
    return randy
    

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    rounds = int(input("How many rounds? Pick a number between 1-9:"))
    return rounds

#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1move, cmove):
    print(p1move + " " + cmove)
    if p1move == cmove:
        return("It's a tie!")
    elif p1move == 'scissors' and cmove == 'paper':
        return("You win!")
    elif p1move == 'paper' and cmove == 'rock':
        return("You win!")
    elif p1move == 'rock' and cmove == 'scissors':
        return("You win!")
    elif p1move == 'rock' and cmove == 'paper':
        return("You lose!")
    elif p1move == 'paper' and cmove == 'scissors':
        return("You lose!")
    elif p1move == 'scissors' and cmove == 'rock':
        return("You lose")
    else:
        return("Error")
    
     
    
#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#     returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(shortmove):
    return 1

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    print("Player has a score of {}".format(pscore))
    print("Computer has a score of {}".format(cscore))
    print(" You have tied {} many times".format(ties))

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    pscore = 0
    cscore = 0
    ties = 0
    rounds = get_rounds()
    for rounds in range(int(rounds)):
        p1move = get_p1_move()
        randy = get_comp_move()
        print("player chose {}".format(p1move))
        print("Computer chose {}".format(randy))
        winner = get_round_winner(p1move,randy)
        if winner == "You win!":
            print("Player won!")
            pscore= pscore+1
        elif winner == "You lose!":
            print("Computer won!")
            cscore= cscore+1
        else:
            ties = ties + 1
            print("It's a tie!")
        print_score(pscore, cscore, ties)

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none
# def test():
#     return 1
# getrounds = (get_rounds())
# p1move = (get_p1_move()) 
# cmove = (get_comp_move())
# winner = (get_round_winner(p1move, cmove))
# print(winner)

rps()