import json

# Define a function to print the student list
def print_student_list(student_list, message):
    print(message)
    for student in student_list:
        print(f"{student['last_name']}, {student['first_name']} : ID = {student['ID']} , Email = {student['email']}")

# Load the JSON file into a Python class list
with open('student.json', 'r') as file:
    student_list = json.load(file)

# Output notification and print the original student list
print_student_list(student_list, "This is the original Student list:")

# Add a new student to the list
new_student = {
    "last_name": "Doe",
    "first_name": "John",
    "ID": "12345",
    "email": "johndoe@example.com"
}
student_list.append(new_student)

# Output notification and print the updated student list
print_student_list(student_list, "This is the updated Student list:")

# Append the new data to the JSON file
with open('student.json', 'w') as file:
    json.dump(student_list, file, indent=4)

# Output notification that the JSON file was updated
print("The .json file was updated.")