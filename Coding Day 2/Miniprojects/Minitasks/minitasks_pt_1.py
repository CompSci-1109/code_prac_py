
# 🐍 PYTHON MINI TASKS
# 🔤 Strings (indexing, reversing, format specifiers)
# Ask for a word and:
# Print the 1st, 3rd, and last letter using indexing.
# Print it reversed using slicing ([::-1]).
# Print the word using an f-string with a message.
# Print it using format().
#
# word=input("Give any word: ")
# print(f"The 1st letter of {word} is: ",word[0])
# print(f"The 3st letter of {word} is: ",word[3])
# print(f"The last letter of {word} is: ",word[-1])
# print(f"The reversed form of the word '{word}' is: ",word[::-1])
# print(f"Good Day, {word}!")
# print(f"hello {word}, I love Chocolate Milkshake!")
# 🔄 Loops
# Write a while loop that keeps asking for numbers until the user types stop. Print the sum.
#version 1:
# given_num=[]
# while True:
#    num = input("Enter any number (s to stop) : ")
#    if num.lower()=="s":
#        break
#    given_num.append(int(num))
#
# print("program stopped upon entering s.")
# print(f"the nos. entered are: {given_num}")
# print(f"The total of all the nos. entered are: ", sum(given_num))

# #version 2:
# num = input("Enter any number (s to stop) : ")
# given_num=[]
# while num.lower() != "s":
#    given_num.append(int(num))
#    num = input("Enter any number (s to stop) : ")
#
# print("program stopped upon entering s.")
# print(f"the nos. entered are: {given_num}")
# print(f"The total of all the nos. entered are: ", sum(given_num))

# Write a for loop to print the multiplication table of a number.
# print("---------TABLES---------")
# numera=int(input("Enter the number you want multiplication table of: "))
# for i in range(10+1):
#      product= numera*i
#      print(f"{numera} x {i} = {product}")
# Write a nested loop to print a triangle of stars:
# *
# **
# ***
# ****

# star="*"
# # my_star=int(input("how many rows u want?: "))
# for row in range(5):
#     print()  #prints the given amount of rows first.
#     for column in range(row+1) :
#         print(star,end="")  #prints the stars acc to the rank of rows including the last no. of row, end="" gives empty string between the star printed

# 📋 Lists
# Create a list of 5 fruits.
# Replace the 2nd fruit.
# Reverse the list.
# Add a fruit.
# Remove one fruit.

# fruits=["apples","bananas","cherries","oranges","pears"]
#
# print(f"The Original list: {fruits}")
#
# fruits[2]="pineapple"
# print(f"The replaced element is: {fruits}")
#
# fruits.reverse()
# print(f"The reversed list is: {fruits} ")
#
# fruits.append("coconuts")
# print(f"The newly updated list is: {fruits} ")
#
# fruits.remove("oranges")
# print(f"The element removed list is: {fruits} ")
# 🔑 Sets
# Create two sets of numbers.
# Find their union, intersection, and difference.
# Add a new number to one set.
# Remove a number safely (without error if it doesn’t exist).
# set_1 = {1,2,3,4,5}
# set_2 = {4,5,6,7,8,9}
#
# print(f"set A: {set_1}")
# print(f"set B: {set_2}")
#
# unidas=set_1.union(set_2)
# print(f"the union of the sets are: {unidas}")
#
# intersect=set_1.intersection(set_2)
# print(f"the intersection of the sets are: {intersect}")
#
# diff= set_1.difference(set_2)
# print(f"set A - set B:{diff}")
#
# symdiff=set_1.symmetric_difference(set_2)
# print(f"set A symm. difference set B:{symdiff} ")

# set_2.discard(8)
# print(f"the set after removing 8 from set B is : {set_2}")

# 🔗 Tuples
# Create a tuple of 5 colors.
# Print the 3rd color.
# Count how many times a color appears.
# Find the index of a given color.

# colors= ("red", "yellow", "orange", "green", "blue","yellow")
# # print(f"The original tuple: {colors}")
# # print(f"The third color of the tuple is: {colors[3]}")
# color_to_check= input("Enter any color from the tuple: ")
#
# if color_to_check not in colors:
#  print(f"{color_to_check} is not in the tuple!")
#
# print(f"the occurrence of {color_to_check} in the tuple is: {colors.count(color_to_check)}")
#
# color_to_check_index= input("Enter any color from the tuple: ")
#
# if color_to_check_index not in colors:
#  print(f"{color_to_check_index} is not in the tuple!")

# print(f"the occurrence of {color_to_check_index} in the tuple is: {colors.index(color_to_check)}")

# 🧮 2D Collections
# Make a 2D list for marks of 3 students in 3 subjects. Print row-wise and column-wise using loops.
# (Note: No 2D sets in Python, because sets 3are unordered and mutable – they can’t hold other sets unless frozen. We use lists/tuples for 2D structures.)

# students= ["Alice","Bob","Mark"]
# subjects= ["Networking","Stats","Java"]
# marks_alice= []
# marks_Bob=[]
# marks_Mark=[]
#
# marks_3=[marks_alice,marks_Bob,marks_Mark]
# temp=0
#
# report_3= [subjects,
#            students,
#            marks_3]
#
# print(f"The Students are: {students}")
# print(f"The subjects are: {subjects}")
#
# while len(marks_alice) in range(3):
#  temp= int(input("Enter marks for Alice: "))
#  marks_alice.append(temp)
#
# print(f"The list of marks for Alice are: {marks_alice}")
#
# while len(marks_Bob) in range(3):
#  temp= int(input("Enter marks for Bob: "))
#  marks_Bob.append(temp)
#
# print(f"The list of marks for Bob are: {marks_Bob}")
#
# while len(marks_Mark) in range(3):
#  temp= int(input("Enter marks for Mark: "))
#  marks_Mark.append(temp)
#
# print(f"The list of marks for Mark are: {marks_Mark}")
#
# print(f"--------------Students with their marks in each subject--------------")
# print(f"{'Students':<10}", end=" ") #prints the word "student" in the header
#
# #this line prints subjects in the header
# for sub in subjects:
#     print(f"{sub:<10}", end=" ")
# print()    # so that it doesn't print continuously after the subject header line
#
# for i in range(len(students)):
#     print(f"{students[i]:<10}",end=" ")  #this loop prints student names below the student column
#
#     for mark in marks_3[i]:              #this loop inside the name printing loop will print marks
#      print(f"{mark:<10}", end=" ")
#     print()



# 📚 Dictionaries
# Create a dictionary of 3 students with name → marks.
# Add a new student.
# Update marks of one student.
# Delete one entry.
# Print all keys and values separately.
student_3=  {"Kay":88,
             "Mikey":79,
             "Vito":68 }

print("The OG Dict:\n")
for key,value in student_3.items():
 print(f"{key}:{value}")
#
# student_3.update({"Tessio":90})
# print(f"\nThe updated dict is: {student_3}")
#
# student_3.update({"Frankie_5_angels":90})
# print(f"\nThe updated dict is: {student_3}")
#
# student_3.pop("Frankie_5_angels")
# print(f"\nLook who betrayed the Corleones!(Hint- they're no longer in this dict) : {student_3}")
#
# student_3.popitem()
# print(f"\nLook who betrayed the Corleones!(Hint- they're no longer in this dict) : {student_3}")
#
# print()
# print("the Keys of Godfather:")
# for key in student_3.keys():
#     print(key)
#
# print("the scores of each Godfather:")
# for val in student_3.values():
#     print(val)
#
# student_3["Mikey"]= 35 #updates just the value of a key specified.
# print(f"\nUpdated marks of mikey:{student_3}")

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
