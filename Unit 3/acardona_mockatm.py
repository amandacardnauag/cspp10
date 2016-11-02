bank_account = int(10000)
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while choice != "3":  #student completes while loop
    if choice == "1": #user chooses 'withdraw'
        #student does this part
        withdraw = input("How much would you like to withdraw? ")
        print (withdraw)
        bank_account = bank_account - int(withdraw)
        print(bank_account)
    elif choice == "2":
        deposit = input("How much to deposit: ")
        print (deposit)
        bank_account = bank_account + int(deposit)
        print(bank_account)
    elif:
        choice == "3" #user chooses 'exit'
    elif:    
        break
        print("Balance: {}".format(bank_account))
        print("1. Withdraw \n2. Deposit \n3. Exit")
        choice = input("Pick from above [1|2|3]:")

    