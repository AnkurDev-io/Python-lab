#Write a program to check whether a given key exists in a dictionary.

subject = {
    "Math":87,
    "English":78,
    "Physics":88,
    "Chemistry":92,
    "CA":100
}

key = input("Enter your key to check existance:")

if key in subject:
    print("key exits")
else:
    print("Not Exists")
    print(subject)