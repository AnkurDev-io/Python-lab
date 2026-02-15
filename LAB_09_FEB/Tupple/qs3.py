# Write a program to check whether a given element exists in a tuple or not.

tupple = (1,3,5,7,9,8)

val = int(input("Enter the value for search element:"))
if val in tupple:
    print("Value exists in tupple")
else:
    print("Not exists!")
    print(tupple)