#user input
first_number=int(input("Enter the first number\n"))
full_name=input("Enter your full name\n")
decimal_number=float(input("Enter the decimal number\n"))

#Display the data type such as int, str,float
print(f"First number is {first_number} and its data type --> {type(first_number)}")
print(f"Full name is {full_name} and its data type --> {type(full_name)}")
print(f"Decimal number is {decimal_number} and its data type --> {type(decimal_number)}")

#Lists
details=["Hrishi", "Dilip", "Ghosalkar", 30, 40, 50]

print(details)
print(type(details))

#tuple

tuple=(1,2,3, "Hrishi", "Ghosalkar")

print(tuple)
print(type(tuple))
