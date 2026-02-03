list1=[12,13,14,15,16]
print("before removing:\n",list1)
value = int(input("Enter the value want to remove:"))

if value in list1:
    list1.remove(value)
    print("After removing",list1)
else:
    print("Value not exists in list")