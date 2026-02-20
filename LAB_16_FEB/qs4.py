# Calculator
a = int(input("Enter a:"))
b= int(input("Enter b:"))
operation = input("Enter your operation want to perform:")

def addition(a,b):
    return a+b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def subtraction(a,b):
    return a-b

if operation.lower()=="add":
    print(addition(a,b))
elif operation.lower()=="sub":
    print(subtraction(a,b))
elif operation.lower()=="mult":
    print(multiplication(a,b))
else:
    print(division(a,b))