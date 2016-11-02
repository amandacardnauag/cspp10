number = input("Enter a non-negative number:")
noun = input("Enter a singular noun:")
n = int(number)
x= 0
if n  == "1":
    print(number + " " + noun)
#Line 6 is the output with the number and the noun. 
else:
    if noun[-2:] == "fe":
        print ("{}{}".format(number,noun[:-2]+"ves"))
    elif noun[-1:] == "y":
# The numbers between the brackets are the numbers last numbers of the word. For examole, when is days "-2" it means that it's reffering to the last two letter of the word.
        print("{}{}".format(number,noun[:-1]+"ies"))
    elif noun[-2:] == "sh" or noun[:-2]=="ch":
# The lines 8-20 are made for nouns that have changes in the ending when being pluralized.
        print("{}{}".format(number,noun +"es"))
    elif noun[-2:] == "us":
        print("{}{}".format(number,noun[:-2]+"i"))
    elif noun[-2:] == "ay" or noun[-2]=="oy" or noun[:-2]=="uy" or noun[:-2]=="ey" :
        print("{}{}".format(number,noun[:-2] +"s"))
    else:
         x= n + " " + noun + "s"
# The 2 lines of code above this line are for the nouns that don't need a change in ending other than adding an s when being pluralized.
    print("{}{}".format(n,noun+"s"))


    