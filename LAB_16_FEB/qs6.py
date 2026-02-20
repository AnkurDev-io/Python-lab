##Write a Python program to calculate the average value of the numbers in a given tuple of
# tuples.
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]

tupple =((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

average = []

for tup in tupple:
    average_marks = sum(tup)/len(tup)
    average.append(average_marks)

print(f"The average marks is:{average}")