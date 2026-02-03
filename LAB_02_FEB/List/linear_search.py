list1 = [2,3,4,5,45,78,23]
key = int(input("Enter the key you want to search:"))
idx = 0
found =0
for i in list1:
    if i==key:
        print(f"Key found at {idx} index")
        found=1
    idx+=1

if found==0:
    print("key Not exits")

    

