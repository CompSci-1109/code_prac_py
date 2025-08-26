
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

# Write a nested loop to print a triangle of stars:
# *
# **
# ***
# ****

# 📋 Lists
# Create a list of 5 fruits.
# Replace the 2nd fruit.
# Reverse the list.
# Add a fruit.
# Remove one fruit.

# 🔑 Sets
# Create two sets of numbers.
# Find their union, intersection, and difference.
# Add a new number to one set.
# Remove a number safely (without error if it doesn’t exist).

# 🔗 Tuples
# Create a tuple of 5 colors.
# Print the 3rd color.
# Count how many times a color appears.
# Find the index of a given color.
# 🧮 2D Collections
# Make a 2D list for marks of 3 students in 3 subjects. Print row-wise and column-wise using loops.
# (Note: No 2D sets in Python, because sets 3are unordered and mutable – they can’t hold other sets unless frozen. We use lists/tuples for 2D structures.)

# 📚 Dictionaries
# Create a dictionary of 3 students with name → marks.
# Add a new student.
# Update marks of one student.
# Delete one entry.
# Print all keys and values separately.

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
