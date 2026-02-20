#Write a program to calculate the sum of the first N natural numbers.
def sum(num):
    sum =0
    for i in range(1,num+1):
        sum+=i
    
    return sum

N = int(input("Enter your number:"))
print(sum(N))
