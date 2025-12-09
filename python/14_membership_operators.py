# Membership operators 
# To check whether a particular value is present or not in a list of sequence 
# Membership operator -- in, not in 

full_name = input("Enter your full name\n")
search_keyword = input("Enter the word to be searched\n")

if search_keyword in full_name:
    print("Keyword found")
else:
    print("Keyword not found")
