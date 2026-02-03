list1=[12,13,14,15,16]
print("Before inserting:",list1)

value = int(input("Enter the value want to insert:"))
idx = int(input("Enter your index:"))

if idx > len(list1)-1:
    print(f"maximum idx:{len(list1)-1}")
else:
    list1.insert(idx,value)
    print("After inserting:\n",list1)