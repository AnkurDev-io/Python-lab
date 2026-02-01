num = int(input("Enter the number:"))

def count_digit(num):
    count = 0
    while num>0:
        last_pos = num %10
        num = num//10
        count+=1
    return count

print(f"The num has {count_digit(num)} digit")