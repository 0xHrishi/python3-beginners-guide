email_format=input("Enter the email address format such as hrishi.ghosalkar or hrishi_ghosalkar\n")

#replace method to replace the dot or underscore with space and title method to capitalize each word 
full_name=email_format.replace("."," ").replace("_", " ").title()

print(f"Your full name is --> {full_name}")
print(f"Your email address is {email_format}@gmail.com")
