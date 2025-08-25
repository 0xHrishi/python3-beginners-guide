#Popular string methods
#strip() --> removes extra space, lower() --> convert into lowercase
#upper() --> Convert into uppercase, title() --> First letter on each word in capital
#capitalize --> First letter in capital, islower() --> Check the string is in lowercase
#is.upper() -> Check string is in upper case, is.title(), is.capitalize()
#is.alpha() --> Check the string contain only aphabets, is.digit(), is.alnum 
#startswith("abc"),endswith("abc")
#repalce("old","new")


full_name=input("Enter your full name\n")

#name in upper case
print(f"Your name in UPPER CASE --> {full_name.upper()}")
#name in lower case
print(f"Your name in lower case --> {full_name.lower()}")
#title method where each word first letter in uppercase
print(f"Your name in title --> {full_name.title()}")
#First word in a sentence is capital
print(f"Your name in capitalize --> {full_name.capitalize()}")

#startswith to check whether a string start with specific keyword defined by the user 
if full_name.startswith("Hri"):
    print("Name starts with Hri")
else:
    print("Name does not start with Hri")

#endwwith to check whether a string ends with specific keyword defined by the user 
if full_name.endswith("kar"):
    print("Name ends with Kar")
else:
    print("Name does not ends with kar")

#startswith to check whether a string is in lowercase
if full_name.islower():
    print("Name is in lower case")
else:
    print("Name is not in lower case")

#startswith to check whether a string is in upper
if full_name.isupper():
    print("Name is in upper case")
else:
    print("Name is not in upper case")

#check whether the string contain only alphabets 
if full_name.isalpha():
    print("Name contain only alphabets")
else:
    print("Name contain alphabets plus other special characters or digits")

#To check whether a string contain an integer or not
number="10"
if number.isdigit():
    print("Number is an integer")
else:
    print("Number is not an integer")

