# ✅ Mini Tasks
# Task 1: Function Basics
# Write a function square(num) that returns the square of a number.
# def square_digit(num):
#     num= float(input("Enter any number:"))
#     sq=  num **2
#     return sq
#
# result=square_digit(2)
# print(f"The square of the given number is: {result:.2f}")

# Task 2: Default Arguments
# Make a function welcome(name="Guest") that prints a welcome message.
# def greet(name="Guest"):
#     if name.strip()=="":
#         name="Guest"
#     print(f"Hello, {name}! Have a nice day! Enjoy the Feast")
#
#
# user_in=input("Enter your name: ")
# # print(f"Hello, {user_in}! Have a nice day! Enjoy the Feast")
#
# greet(user_in)


# Task 3: Keyword Arguments
# Make a function order(food, drink) and call it using keyword arguments.
def menu(food, drink, snack):
     # food= input("Enter the food you want: ")
     # drink= input("Enter the drink you want: ")
     print(f"Food you want :{food}")
     print(f"Drink you want :{drink}")
     print(f"Snack you want: {snack}")

menu(drink= "buttermilk", snack="bhelpuri", food="aloo paratha")




# Task 4: *args
# Write a function multiply(*args) that multiplies all numbers given.


# Task 5: **kwargs
# Make a function student(**kwargs) that prints student details like name, age, grade.

# 🎯 Mini Project – Student Marks Analyzer
# Use everything you’ve learned till now (loops, conditionals, lists, functions, args/kwargs).

# Problem:
# Make a program where:
# You enter marks of students (any number).
# Write a function that calculates:
# Average marks
# Highest marks
# Lowest marks
# Use *args for marks input.
# Use **kwargs for student details.