from pprint import pprint
def dictionary():
    d = {}
    while True:
        u = input("What would you like to do? Add? Delete? Modify? Or exit?")
        if u == 'add':
            x = input("What would you like the key to be called?")
            if x in d:
                print("This key already exists.")
            y = input("What would you like the value of the key to be?")
            d[x] = y
            pprint (d)
        if u == 'delete':
            k = input("What key would you like to delete?")
            if k in (d): 
                del d[k]
            else:
                print("Sorry, key was not found.")
            pprint (d)
        if u == "modify":
            x = input("What would you like to modify?")
            if x in (d):
               m = input("What would you like to change the value to?")
               d[x] = m
               pprint(d)
        if u == 'Exit':
            print("Exit")
            break
dictionary() 