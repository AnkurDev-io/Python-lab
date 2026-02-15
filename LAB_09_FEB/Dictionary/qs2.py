# Write a program to add a new key-value pair to an existing dictionary.


student = {
    "name":"Ankur Dutta",
    "roll":68,
    "cgpa":8.43
}

keys = input("Enter your key to add:")
values = input("Enter your value to add:")

if values.isdigit():
    values = int(values)
    student.update({keys:values})
    print(student)
else:
 student.update({keys:values})
 print(student)