num = int(input("Enter the number:"))

def calculate_reverse(num):
    reverse =0
    while num>0:
        last_pos = num %10
        reverse=reverse*10+last_pos
        num =num//10
    return reverse

reversed_num = calculate_reverse(num)
print(f"reversed no is :{reversed_num}")