#!/usr/bin/python

#script to add two numbers i.e. first_number and second_number 
#result is odd or even 

#user input 
first_number=input("Enter the first number:\n")
second_number=input("Enter the second number:\n")

#function
def lines():
    print("*"*30)

#Check the user input is empty and if yes, display error message
if (len(first_number)==0) or (len(second_number)==0):
    if (len(first_number)>0) and (len(second_number)==0):
        lines()
        print("Second number field is empty")
    elif (len(first_number)==0) and (len(second_number)>0):
        lines()
        print("First number field is empty")
    elif (len(first_number)==0) and (len(second_number)==0):
        lines()
        print("First number field is empty")
        print("Second number field is empty")
    else:
        lines()
        print("Issues with user input")

#user input is not empty
elif (len(first_number)>0) and (len(second_number)>0):

    #Check user input must contain only numeric values no alphabets
    if not first_number.isdigit() or not second_number.isdigit():
        if first_number.isdigit() and not second_number.isdigit():
            lines()
            print("Second number field must contain only numeric values")
        elif not first_number.isdigit() and second_number.isdigit():
            lines()
            print("First number field must contain only numeric values")
        elif not first_number.isdigit() and not second_number.isdigit():
            lines()
            print("First number field must contain only numeric values")
            print("Second number field must contain only numeric values")
        else:
            lines()
            print("Issues with the user input validation")

    #user input contain only numeric values
    elif first_number.isdigit() and second_number.isdigit():
        sum=int(first_number)+int(second_number)
        if (int(sum)%2==0):
            lines()
            print(f"Additon of {first_number} and {second_number} --> {sum}")
            print(f"{sum} --> Even number")
        elif (int(sum)%2!=0):
            lines()
            print(f"Additon of {first_number} and {second_number} --> {sum}")
            print(f"{sum} --> Odd number")
        else:
            lines()
            print("Issues with calculation")
