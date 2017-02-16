from pprint import pprint
def dictionary():
    u = input("What would you like to do? Add? Delete? Or exit?")
    d = {}
while True:
    if u == 'add':
        x = input("What would you like the key to be called?")
        y = input("What would you like the value of the key to be?")
        pprint (d)
    if u == 'delete':
        k = input("What key would you like to delete?")
    if k in (d):
        del d[k]
        pprint (d)
    else:
        print("Exit")
        break
dictionary() 