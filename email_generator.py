#Python script which takes username as input and display email address
email_name=input("Enter email name, example --> hrishi.ghosalkar or hrishi_ghosalkar\n")

#strings --> replace method to replace dot or underscore with space and title to capitalize each word
full_name=email_name.replace(".", " ").replace("_", " ").title()

email_address=f"{full_name}@gmail.com"

print(f"Your full name is {full_name}")
print(f"Your email address is --> {email_address}")

print("\n")
print(f"""Dear {full_name}
Your complete email address is {email_address}.
Best regards
""")
