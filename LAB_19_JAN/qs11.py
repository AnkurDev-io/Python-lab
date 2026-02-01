num = int(input("Enter the number:"))

def calculate_factorial(num):
    fact =1
    for i in range(1,num+1):
        fact*=i
    return fact

print(f"Factorial of {num} is {calculate_factorial(num)}")