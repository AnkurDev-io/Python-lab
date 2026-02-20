def fibonacci_series(num):
    if num ==0:
        return 0
    elif num ==1:
        return 1
    else:
        return fibonacci_series(num-1)+fibonacci_series(num-2)
    
N = int(input("Enter your number:"))
for i in range(N):
    print(fibonacci_series(i),end=" ")