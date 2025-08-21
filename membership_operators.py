#Membership operator 
# in, not in 

full_name=input("Enter full name\n")
keyword=input("Enter the keyword to find\n")

if keyword in full_name:
    print(f"Keyword --> {keyword} found in Full name --> {full_name}")
else:
    print(f"Keyword --> {keyword} not found in Full name --> {full_name}")
