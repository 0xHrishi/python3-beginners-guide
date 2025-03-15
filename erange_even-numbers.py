#!/usr/bin/python

#user input first and second number
#print even or odd numbers 

import time

#User input
first_number=input("Enter first number:\n")
second_number=input("Enter second number:\n")

def lines():
    print("*"*40)

#user input length empty
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
        print("Issues with the user input")

#User input is not empty
elif len(first_number)>0 and len(second_number)>0:
    
    #check user input must contain only numeric values
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
            print("Issues with the user input")

    #user input only nuemric values
    elif first_number.isdigit() and second_number.isdigit():
        if int(first_number)<int(second_number):
            opinion=input("Would you like to print even or odd number\n")
            if str(opinion)=="even":
                lines()
                for even_numbers in range(int(first_number),int(second_number)+1):
                    if (int(even_numbers)%2==0):
                        lines()
                        print(f"Even number --> {even_numbers}")
                    else:
                        time.sleep(1)
                        continue
            elif str(opinion)=="odd":
                lines()
                for odd_numbers in range(int(first_number),int(second_number)+1):
                    if (int(odd_numbers)%2!=0):
                        lines()
                        print(f"Odd number --> {odd_numbers}")
                    else:
                        time.sleep(1)
                        continue
            else:
                lines()
                print("Issues with the user input")

        elif (int(first_number)>int(second_number)):
            lines()
            print("First number cannot be greather than second number")
        elif (int(first_number)==int(second_number)):
            lines()
            print("First number equal to second number")
            print("Nothing can be done")

