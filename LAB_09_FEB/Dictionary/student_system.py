#Write a menu-driven program using dictionary:

# Add student

# Delete student

# Display all students

# Exit

student = {}

while True:

    print("\n--- Student Management Menu ---")
    print("1. Add student")
    print("2. Delete student")
    print("3. Display all students")
    print("4. Exit")

    choice = int(input("Enter your choice"))

    # add Student

    if choice == 1:
        roll = int(input("Enter roll no:"))
        name = input("Enter student name:")
        student[roll]=name
        print("Student added successfullu")
        print(student)
    
    ## Delete Student
    if choice ==2:
        roll = int(input("Enter roll no for search:"))
        if roll in student:
            student.pop(roll)
            print("Student deleted successfully")
            print(student)
        else:
            print("Student not found")
    
    ## display Students
    if choice == 3:
        if student:
            print("\nRoll No\tName")
            for roll, name in student.items():
                print(roll, "\t", name)
        else:
            print("No students to display.")

    ## 
    ## exit program

    if choice == 4:
        print("Programme exiting......")
        break

