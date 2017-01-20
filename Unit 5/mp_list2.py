userinput = 1

userlist = []
print("Please choose sum, clear, print, length or exit.")
while userinput is not 0:
    userinput= input("Choose one or enter a number:")

    if userinput == "print":
        print(userlist)
    elif userinput == "clear":
        userlist = []
        print (userlist)
    elif userinput == "exit":
        print ("End")
        break
    elif userinput == "length":
        print(len(userlist))
    elif userinput == "sum":
        print(sum(userlist))
    else:
        userinput = int(userinput)
        userlist.append(userinput)