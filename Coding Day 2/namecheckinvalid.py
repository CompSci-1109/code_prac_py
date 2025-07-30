print("The username should NOT: "
      "\n1.Contain more than 12 characters."
      "\n2.Contain spaces."
      "\n3.Contain Digits. ")

name= str(input("Enter your username:"))

has_Digit=False
has_Space=False
has_char12=False

if len(name) >12:
    has_char12=True

for alph in name:
    if alph.isdigit():
        has_Digit=True
    elif alph.isspace():
        has_Space=True
if has_char12 or has_Digit or has_Space:
    print("The Username must have no numbers, spaces and must be lesser than 12 characters.\n")
else:

    if has_char12:
      print("The Username must not be longer than 12 characters.")
    if has_Digit:
      print("The username must not have numbers.")
    if has_Space:
      print("The username cannot have spaces.")
else:
    print("Username Accepted.")

