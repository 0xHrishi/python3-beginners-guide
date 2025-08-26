#Popular string methods 
#string.lower() --> Convert the string into lowercase 
#string.upper() --> Convert the string into uppercase
#string.title() --> First letter in each word 
#string.capitalize() --> First letter capital 
#string.repalce("old","new") --> Replace the string with a new word
#string.find("Hri") --> Helps the user to find a keyword is present or not within specific string
#string.split("@")[0] --> Spilt the string based upon the user specific word and display as per index
#string.strip() --> Remove extra spaces 
#string.lstrip() and string.rstrip() --> Removes extra spaces from left to right 

#string.startswith() and string.endswith() --> Confirm whether the staring starts and ends with a specific keyword 

#Verify string 
#isupper() --> Check whether the string is in uppercase format
#islower() --> Check whether the string is in lowercase format
#isdigit() --> Check whether the string contains only nuemric values
#isalnum --> Check whether string contains alphabets and numeric values
#isalpha() --> String must contain only alphabets

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

