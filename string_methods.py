# Popular string methods
# str.lower -- convert the string into lowercase
# str.uppercase -- convert the string into uppercase
# str.title -- First letter of each word in Capital 
# str.capitalize -- Only first letter of an sentence is Capital
full_name = input("Enter the full name\n")

print(f"Full name in uppercase -- {full_name.upper()}")
print(f"Full name in lowercase -- {full_name.lower()}")
print(f"Full name in title format -- {full_name.title()}")
print(f"Full name in capitalize -- {full_name.capitalize()}")
######################################################################################################################################################
# str.isalpha() -- Validates a string i.e. it contains only alphabets
# str.isalnum() -- Validates a string i.e. it contains alphabets and numeric values, No spaces, no dots, no special characters
# str.digit() -- Validates a string i.e. it contains numeric values
# str.islower() -- Check the string, str.isupper()
if full_name.isalpha():
    print("String contains only alphabets")
else:
    print("String contains more than just characters")

if full_name.isalnum():
    print("String contains alphabets and numeric values")
else:
    print("String does not contains alphabets and numeric values")

if full_name.isdigit():
    print("Numeric value detected")
else:
    print("Numeric value not detected")
######################################################################################################################################################
# str.lstip() -- Remove extra spaces at beginning 
# str.rstrip() -- Remove extra spaces at the ending 
# str.strip() -- Remove beginning and ending extra spaces 

print(f"Removing beginning extra spaces {full_name.lstrip()}")
print(f"Removing ending extra spaces {full_name.rstrip()}")
print(f"Removing beginning and ending extra spaces {full_name.strip()}")
######################################################################################################################################################
# strs.endswith() -- Check whether a string ends with user specified letters
# strs.startswith() -- Check whether a string starts with user specified letters
# strs.startswith("abc", "xyz") -- Multiple checks

if full_name.startswith("hri"):
    print("String starts from hri")
else:
    print("String does not starts from hri")

if full_name.endswith("hri"):
    print("String ends from hri")
else:
    print("String does not ends from hri")
######################################################################################################################################################
# str.replace -- abc gets replaced by ayx
str.replace("abc","ayx")
