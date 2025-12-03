# Popular string methods
full_name = input("Enter your full name\n")


# str.upper() -- Convert the string to uppercase, str.lower() -- Convert the string to lowercase
# str.title() -- First letter in each word is capital, str.capitalize() -- First letter in a sentence is capitalize
# str.strip() -- Removes extra spaces from left and right, str.rstrip() -- Remove extra spaces from right 
# str.lstrip() -- Remves extra spaces from left 
print(f"Your full name in upper case -- {full_name.upper()}")
print(f"Your full name in lower case -- {full_name.lower()}")
print(f"Your full name in title format -- {full_name.title()}")
print(f"Your full name in Capitalize -- {full_name.capitalize()}")
print(f"Lets remove the extra spaces from left -- {full_name.lstrip()}")
print(f"Lets remove the extra spaces from right -- {full_name.rstrip()}")
print(f"Lets remove the extra spaces from left and right -- {full_name.strip()}")

print("*"*100)

# str.endswith() -- Used to check whether a string ends with specfic word or letter
# str.endswith("abc") or str.endswith(full_name) 
# str.endswith("abc", "xyz") or str.endswith(full_name, first_name)
if full_name.endswith("abc"):
    print("Ok")
else:
    print("No OK")

# str.startswith() -- Used to check whether a string starts with specfic word or letter
# str.startswith("abc") or str.startswith(full_name) 
# str.startswith("abc", "xyz") or str.startswith(full_name, first_name)
if full_name.startswith("abc"):
    print("Ok")
else:
    print("No OK")

# str.replace -- Replace the string if match is found
# str.replace("abc", "xyz") or str.replace(full_name, first_name)
if full_name.startswith("abc"):
   print(full_name.replace(full_name, "xyz"))
else:
    print("No OK")

# Check user input
# str.isupper -- Check whether the string is in uppercase
# str.islower -- Check whether the string is in lowercase
# str.isalpha -- Check whether the string contains on alphabets
# str.isalnum -- Check string consists of nuberrs or alphabets
# str.isdigit -- Check string consists of numbers only










