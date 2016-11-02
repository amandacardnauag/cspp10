import random
randomnum = (random.randint(0,101)) 
numg = 0
num = int(input(" Guess a number between 1-100:"))
numg = numg + 1 
while num >= 1 and num <= 100:
    if num < randomnum:
        print ("Too low! Try again.")
        num = int(input(" Guess a number between 1-100:"))
        numg = numg + 1 
    elif num > randomnum:
        print("Too high! Try again.")
        num = int(input(" Guess a number between 1-100:"))
        numg = numg + 1 
        
    elif num == randomnum:
        print ("You got it, dude!")
        print (" It took you {} tries".format(numg))
        break
    