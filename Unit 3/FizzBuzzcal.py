num = int(input("Enter a number:"))
for n in range(1, num + 1):
    if 0 == n % 3 and 0 == n % 5:
        print("FizzBuzz")
    elif 0 == n % 3: 
        print ("fizz")
    elif 0 == n % 5:
        print("buzz")
    else:
        print(n)