#Popular string methods
full_name = "ADADA ADADA ADADA"

#Converts the string into lower case
print(f"lower case -- {full_name.lower()}")

#Converts the string into upper case
print(f"Upper case -- {full_name.upper()}")

#First letter of each word in capital
print(f"Title -- {full_name.title()}")

#First letter capital
print(f"Capitalize -- {full_name.capitalize()}")

#condition to check whether the full name is in lowercase
if full_name == full_name.lower():
    print("OK")
else:
    print("Not OK")

#condition to check whether the full name is in upper
if full_name == full_name.upper():
    print("OK")
else:
    print("Not OK")

#startswith and endswith 
#Multiple -- if full_name == full_name.startswith(("adada", "asfdfsf")):
if full_name == full_name.startswith("adada"):
    print("OK")
else:
    print("Not OK")

#strip() -- Removes the front and end extra spaces
#lstrip() -- Removes the spaces from left
#rstrip() -- Removes the spaces from right 
#string.find 
