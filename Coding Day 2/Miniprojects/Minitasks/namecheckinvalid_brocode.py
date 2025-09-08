username= input("Enter Username: ")

if len(username)>12:
    print("The username must not be longer than 12 characters.")
elif not username.find(" ") == -1:
    print("Username cannot have spaces.")
elif not username.isalpha():
    print("Username cannot have numbers.")
else:
    print(f"Welcome{username}")