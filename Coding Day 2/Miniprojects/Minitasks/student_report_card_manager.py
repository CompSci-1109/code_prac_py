# FINAL BOSS 🤖:
# 🐍 Mini Project (Python)
# Student Report Card Manager
# Store multiple students with their marks (dictionary → values as lists).

# Allow the user to:
# Add a student with marks.
# Update marks.
# Print average marks of a student.
# Print all students with marks.
# Use loops, lists, dict methods, and string formatting.


print("---------------STUDENT REPORT CARD MANAGER---------------")


students= {"Sana":[89,85,81,84,82,83], "Ayesha":[89,87,88,86,83,85], "Chandana":[85,78,87,86,85,80], "Vito":[75,78,80,81,83,74,76], "Tim":[76,78,75,74,80,79]}

userName= input("Enter Your name:")
print(f"Hello,{userName}!")


print("1. Add a student with marks. \n 2. Update marks of a student. "
      "\n 3. Find Average marks of a student. \n 4.Find all students' marks. \n 5. Exit.")
opt_num= int(input("Enter the option number of the task you wanna proceed with."))

if opt_num==1:
     print("\nYou chose: 1. Add a student with marks.")
     new_Student= input("\nEnter the student name whose marks you sish to add.")
     marks_Stud_new= int(input("Enter the marks of the student , seperated with spaces"))
     marks_Stud_list= [int(marks_Stud_new) for mark in marks_Stud_new]

     students.update({new_Student:marks_Stud_list})

