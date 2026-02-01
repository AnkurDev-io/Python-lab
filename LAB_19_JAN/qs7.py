#calculator
a = int(input("Enter First number:"))
b = int(input("Enter First number:"))
opration =input("Enter what operation you perform:")

if opration.lower() == "add":
    print(a+b)
elif opration.lower() =="mult":
    print(a*b)
elif opration.lower()=="div":
    print(a/b)
else:
    print(a-b)


