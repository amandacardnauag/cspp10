userinput = 1

print ("Please choose sum, clear, print, length or exit.")
userinput= input("Choose one or enter a number:")
print userinput

userlist = []
while True: 
    if userinput == 0:
        print "Game over"
        break