# Write a program to remove duplicate elements from a list using a set.

list1 = [1,1,3,4,3,5,5,4,6]

unique_elements = list(set(list1))
print(f"Original list : {list1}")
print(f"After removing duplicates elemnts:{unique_elements}")
