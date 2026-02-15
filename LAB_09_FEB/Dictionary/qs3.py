# Create a dictionary of 5 subjects and their marks.
# Calculate the total and average marks.

subject = {
    "Math":87,
    "English":78,
    "Physics":88,
    "Chemistry":92,
    "CA":100
}

marks = subject.values()
list1 = list(marks)
print(f"The sum of all marks in the dict:{sum(list1)}")
print(f"The Average marks:{sum(list1)/len(list1)}")