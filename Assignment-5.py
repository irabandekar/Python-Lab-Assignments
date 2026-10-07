import re

s = input("Enter a string: ")

if re.fullmatch("[a-zA-Z0-9]+", s):
    print("Valid String")
else:
    print("Invalid String")
