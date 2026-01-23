# Popular string methods

#!/usr/bin/python
def lines():
    print("*"*50)

sentence = input("Enter any sentence:\n")
lines()
# str.lower() -- converts the string into lowercase
# str.upper() -- converts the string intp uppercase
# str.title() -- in title format i.e. first letter in each word is capital
# str.capitalize() -- in capitalize format i.e. first letter in the sentence is in capital
print(f"Name in lowercase --> {sentence.lower()}")
print(f"Name in Upper --> {sentence.upper()}")
print(f"Name in title --> {sentence.title()}")
print(f"Name in capitaliaze --> {sentence.capitalize()}")

# str.lstrip() -- Remove the extra spaces from the left
# str.rstrip() -- Remove the extra spaces from the right
# str.strip() -- remove the leading and trailing extra spaces
print(f"Remove the extra spaces from left -- {sentence.lstrip()}")
print(f"Remove the extra spaces from right -- {sentence.rstrip()}")
print(f"Remove the extra spaces from left and right -- {sentence.strip()}")+

# check whether a string starts with a specific keyword i.e. str.startswith("keyword")
# str.startswith("abc") and str.startswith("abc","xyz")
# str.startswith(var_1) and str.startswith(var_1,var_2)

# check whether a string ends with a specific keyword i.e. str.endswith("keyword")
# str.endswith("abc") and str.endswith("abc","xyz")
# str.endswith(var_1) and str.endswith(var_1,var_2)
if sentence.startswith("abc"):
    print(f"Sentence starts with the specified keyword")
else:
    print(f"Sentence does not starts with the specified keyword")
if sentence.endswith("abc"):
    print(f"Sentence ends with the specified keyword")
else:
    print(f"Sentence does not ends with the specified keyword")

# verify the user input
str.islower() -- Check whether the string is in lowercase
str.isupper() -- Check whether the string is in uppercase
str.istitle() -- Check each word is capital 
str.isdigit() -- Check whether the string contain numeric values
str.isalpah() -- Check whether the string contain alpahbets
str.isalnum() -- Check whether the string contain alphabets and numeric 

# str.replace() -- Replace the word
str.replace(".", “ ”) -- Replace the dot ‘.’ with space 
str.reaplce(name_1, name_2)
	
    
    





