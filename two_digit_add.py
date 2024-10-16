#python3 basic script to add two digit. Two digit from the user input
#isdigit method to check the user input is only numeric

#!/usr/bin/python3

two_digits=input("Enter the two digits number\n")


if len(two_digits)==0:
    print("*"*50)
    print("User input empty")
else:
    if not two_digits.isdigit():
        print("*"*50)
        print("Field must contain numeric digits only")
    else:
        first_digit=two_digits[0]
        second_digit=two_digits[1]
        ans=int(first_digit)+int(second_digit)
        print("*"*50)
        print(f"{first_digit} plus {second_digit} --> {ans}")
