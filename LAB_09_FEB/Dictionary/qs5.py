# Create a dictionary and:

# Delete a key

# Update a value


subject = {
    "Math":87,
    "English":78,
    "Physics":88,
    "Chemistry":92,
    "CA":100
}

## delete a key 

key = input("Enter your key name:")
if key in subject:
    subject.pop(key)
    print(subject)

## Update a key 

key_forUpdate = input("Enter your key name for update:")

if key_forUpdate in subject:
    value = int(input("Enter value for update:"))
    subject[key_forUpdate] = value
    print(subject)
else:
    print("Key not found in the dict")