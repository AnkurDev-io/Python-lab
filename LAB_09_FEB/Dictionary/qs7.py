# Write a program to sort a dictionary by its keys.

subject = {
    "Math":87,
    "English":78,
    "Physics":88,
    "Chemistry":92,
    "CA":100
}

sorted_keys = sorted(subject.keys())
sorted_dict = {}
for i in sorted_keys:
    sorted_dict[i] = subject[i]

print(sorted_dict)
