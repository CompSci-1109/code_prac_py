print("The username should NOT: "
      "\n1.Contain more than 12 characters."
      "\n2.Contain spaces."
      "\n3.Contain Digits. ")

name= str(input("Enter your username:"))

# has_Digit=False
# has_Space=False
# has_char12=False

if len(name) >12:
    print("The Username cannot be longer than 12 characters.")

for alph in name:
    if alph.isdigit():
        print("The username must not have numbers.")
    elif alph.isspace():
        print("The username cannot have spaces.")
if alph.isdigit() or alph.isspace():
    print("Username Not Accepted.")
#     if has_char12:
#       print("The Username must not be longer than 12 characters.")
#     if has_Digit:
#       print("The username must not have numbers.")
#     if has_Space:
#       print("The username cannot have spaces.")
else:
      print("Username Accepted.")

