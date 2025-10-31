#Popular string methods
full_name = "ADADA ADADA ADADA"

# Converts the string into lower case
print(f"lower case -- {full_name.lower()}")

# Converts the string into upper case
print(f"Upper case -- {full_name.upper()}")

# First letter of each word in capital
print(f"Title -- {full_name.title()}")

# First letter capital
print(f"Capitalize -- {full_name.capitalize()}")

# condition to check whether the full name is in lowercase
full_name=input("Enter your name\n")

if full_name.islower():
    print("lowercase")
else:
    print("Not lowercase")

# condition to check whether the full name is in upper
full_name=input("Enter your name\n")

if full_name.isupper():
    print("uppercase")
else:
    print("Not upper case")

# startswith and endswith 
#Multiple -- full_name.startswith(("adada", "asfdfsf")):
full_name=input("Enter your name\n")

if full_name.startswith("Abc"):
    print("ok")
else:
    print("Not ok")

# endswith
full_name=input("Enter your name\n")

if full_name.endswith("Abc"):
    print("ok")
else:
    print("Not ok")

# strip() -- Removes the front and end extra spaces
# lstrip() -- Removes the spaces from left
# rstrip() -- Removes the spaces from right 
full_name=input("Enter your name\n")

print(f"Name is {full_name}")
print(f"Name is {full_name.strip()}")

# is.alpha(), is.digit(), is.alnum(), is.title(), 
full_name=input("Enter your name\n")

if full_name.isalpha():
    print("ok")
else:
    print("Not ok")

