noun = input("Enter a singular noun:")
number = input("How many of {}? ".format(noun))

if number == "1":
    print("1 " + noun)
#Line 6 is the output with the number and the noun. 
else:
    if noun[-2:] == "fe":
        print(number + " " + noun[:-2] + "ves") 
    elif noun[-1:] == "y":
# The numbers between the brackets are the numbers last numbers of the word. For examole, when is days "-2" it means that it's reffering to the last two letter of the word.
        print(number + " " + noun[:-1] + "ies")
    elif noun[-2:] == "sh" or noun[-2:]=="ch":
# The lines 8-20 are made for nouns that have changes in the ending when being pluralized.
        print(number + " " + noun + "es") 
    elif noun[-2:] == "us":
        print(number + " " + noun[:-2] + "i")
    elif noun[-2:] == "ay" or noun[-2:] == "oy" or noun[-2:] == "ey" or noun[-2:] == "uy": 
          print(number + " " + noun + "s")
    else:
         print(number + " " + noun + "s"
# The 2 lines of code above this line are for the nouns that don't need a change in ending other than adding an s when being pluralized.
     


    