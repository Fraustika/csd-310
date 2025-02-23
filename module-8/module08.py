import json

# Function to load the JSON file into a Python class list
def load_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to print the student list
def print_student_list(student_list):
    for student in student_list:
        print(f"{student['last_name']}, {student['first_name']} : ID = {student['id']} , Email = {student['email']}")

# Function to save the updated list back to the JSON file
def save_json_file(filename, student_list):
    with open(filename, 'w') as file:
        json.dump(student_list, file, indent=4)

# Load the original student list
filename = 'student.json'
students = load_json_file(filename)

# Notify and print the original student list
print("This is the original Student list:")
print_student_list(students)

# Append new student data
new_student = {
    "last_name": "Doe",
    "first_name": "John",
    "id": "99999",
    "email": "johndoe@example.com"
}
students.append(new_student)

# Notify and print the updated student list
print("\nThis is the updated Student list:")
print_student_list(students)

# Save the updated list back to the JSON file
save_json_file(filename, students)

# Notify that the JSON file was updated
print("\nThe .json file was updated.")