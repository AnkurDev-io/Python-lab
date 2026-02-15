# 4. Create a tuple of numbers and:

# Convert it into a list
# Add a new element
# Convert it back into a tuple

tupple = (1,3,4,5,6,7,9,10)
list1 = list(tupple)
print(f"After converting tupple to list:{list1}")

val = int(input("Enter the value to add in tupple:"))
tupple = tupple+(val ,)
print(f"After adding element:{tupple}")

print(f"list to tupple:{tuple(list1)}")
