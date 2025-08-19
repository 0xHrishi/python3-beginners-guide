first_number=int(input("Enter first number\n"))
second_number=int(input("Enter second number\n"))

#Comparsion operator
# > greater than, >= greater than equal to
# < less than, <= less than equal to
# == equal to, != not equal to

if first_number > second_number:
    print(f"First number:{first_number} is greater than second number:{second_number}")
elif first_number < second_number:
    print(f"First number:{first_number} is less than second number:{second_number}")
elif first_number == second_number:
    print(f"First number:{first_number} is equal to second number:{second_number}")
else:
    print("Something went wrong")
