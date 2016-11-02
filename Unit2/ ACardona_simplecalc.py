oper = input("Enter your equation:")
first_term = oper[0]
operation = oper[1]
second_term = oper[2]
f = int(first_term)
s = int(second_term)
x = 0
if operation == "+":
    x = f + s
elif operation == "-":
    x == f - s
elif operation == "/":
    x == f / s
elif operation == "*":
    x == f * s
elif operation == "%":
    x == f % s
else: 
    print (" Input is invalid")

print (" Your answer is {}".format(x))    
    
    