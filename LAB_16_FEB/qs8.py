tupple = ()
print("add Elemnt in the tupple\n")

for i in range(5):
    val = int(input(f"{i}th element: "))
    tupple += (val ,)

#get 4th elemmnt from the last

print(f"The 4th elemnt is{tupple[-4]}")