# Popular string methods
# str.lower() -- Convert the string into lowercase
# str.upper() -- Convert the string into uppercase
# str.title() -- First letter of each word -- capital
# str.capitalize() -- First letter in a sentence -- Capital 
full_name = input("Enter your full name\n")

print(f"Your name is {full_name.lower()}")
print(f"Your name is {full_name.upper()}")
print(f"Your name is {full_name.title()}")
print(f"Your name is {full_name.capitalize()}")

# str.islower() -- Check whether the string is in lowercase
# str.isupper() -- Check whether the string is in uppercase
# str.istitle() -- Check whether the string is in title format
if full_name.islower():
    print("lowercase")
else:
    print("Not in lowercase")

if full_name.isupper():
    print("uppercase")
else:
    print("Not in uppercase")

if full_name.istitle():
    print("title format")
else:
    print("Not in title format")
lines()

# str.isalpha() -- Check whether the string consist of only alphabets
# str.isdigit() -- Check whether the string consist of only digits
# str.isalnum() -- Check whether the string consist of alphabets or digits

if full_name.isalpha():
    print("All alphabets")
else:
    print("not alphabets")
if full_name.isdigit():
    print("All digits")
else:
    print("not digits")
if full_name.isalnum():
    print("All alphanumeric")
else:
    print("not alphanumeric")


# str.startswith("abc") -- Help the user to check whether a string starts with specific keyword
# str.startswith(("abc", xyz)) -- Help the user to check whether a string starts with specific keyword
# str.endswith("abc") -- Help the user to check whether a string ends with specific keyword
# str.endswith(("abc", xyz)) -- Help the user to check whether a string starts with specific keyword
name = input("Enter name\n")

if name.endswith(("Hri","hri")):
    print("Name starts with specified keyword")
else:
    print("Name does not starts with specified keyword")

name = input("Enter name\n")

if name.endswith(("Hri","hri")):
    print("Name starts with specified keyword")
else:
    print("Name does not starts with specified keyword")

# str.strip -- Remove leading and trailig extra spaces
# str.lstrip() -- remove leading extra spaces
# str.rstrip() -- remove trailing spaces

# str.repalce("abc", "xyz) -- Allows the user to replace a specific keyword
