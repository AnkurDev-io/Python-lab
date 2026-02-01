marks = int(input("Enter your marks:"))

if marks <0:
    print(f"Marks should not be negative")
else:
    if marks >=90 and marks<=100:
        print("Your grade is A")
    elif marks<90 and marks >=75:
        print("Your garde is B")
    elif marks<75 and marks>=60:
        print("Your garde is C")
    elif marks<60 and marks >=40:
        print("Your garde is D")
    else:
        print("Fail")
