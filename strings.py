full_name=input("Enter your full name\n")

#Print function to display the text
print(full_name)

#Concatenation
print("Your full name is " + full_name)
#formated strings
print(f"Your full name is {full_name}")
print("\n")

#Popular string methods
#upper and lower case, title, capitalize
print(f"Your full name using uppercase string method -->  {full_name.upper()}")
print(f"Your full name using lowercase string method -->  {full_name.lower()}")
print(f"Your full name using title string method -->  {full_name.title()}")
print(f"Your full name using capitalize method -->  {full_name.capitalize()}")

#string methods startswith and endswith
if full_name.startswith("Hri"):
    print("ok")
else:
    print("Not ok")

if full_name.endswith("kar"):
    print("ok")
else:
    print("Not ok")

#isalpha, isdigit, isalnum, islower, isupper, islower, isupper
if full_name.isalpha():
    print("ok")
else:
    print("No ok")

if full_name.isdigit():
    print("ok")
else:
    print("No ok")

if full_name.isalnum():
    print("ok")
else:
    print("No ok")

if full_name.islower():
    print("ok")
else:
    print("No ok")

if full_name.upper():
    print("ok")
else:
    print("No ok")
