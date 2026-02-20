# Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

list1 =  [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list =[]
for t in list1:
    print(t[:-1])
    new_tupple = t[:-1]+(100, )
    new_list.append(new_tupple)

print(new_list)
