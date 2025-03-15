#!/usr/bin/python
#user input first number, multiplier, stop number
# first number times the multiplier until the result reaches the stop number
import time

#user input
first_number=input("Enter the first number\n")
multiplier=input("Enter the multiplier number\n")
stop_number=input("Enter the stop number\n")

#function
def lines():
    print("*"*30)

#Check user input, if empty
if (len(first_number)==0) or (len(multiplier)==0) or (len(stop_number)==0):
    if (len(first_number)>0) and (len(multiplier)>0) and (len(stop_number)==0):
        lines()
        print("Stop number field is empty")
    elif (len(first_number)>0) and (len(multiplier)==0) and (len(stop_number)==0):
        lines()
        print("Multiplier number field is empty")
        print("Stop number field is empty")
    elif (len(first_number)>0) and (len(multiplier)==0) and (len(stop_number)>0):
        lines()
        print("Multiplier number field is empty")
    elif (len(first_number)==0) and (len(multiplier)==0) and (len(stop_number)>0):
        lines()
        print("First number field is empty")
        print("Multiplier number field is empty")
    elif (len(first_number)==0) and (len(multiplier)>0) and (len(stop_number)>0):
        lines()
        print("First number field is empty")
    elif (len(first_number)==0) and (len(multiplier)>0) and (len(stop_number)==0):
        lines()
        print("First number field is empty")
        print("Stop number field is empty")
    elif (len(first_number)==0) and (len(multiplier)==0) and (len(stop_number)==0):
        lines()
        print("First number field is empty")
        print("Multiplier number field is empty")
        print("Stop number field is empty")
    else:
        lines()
        print("Issues with the user input")

#user input is not empty
elif (len(first_number)>0) and (len(multiplier)>0) and (len(stop_number)>0):

    #user input must contain only numeric values
    if not first_number.isdigit() or not multiplier.isdigit() or not stop_number.isdigit():
        if  first_number.isdigit() and multiplier.isdigit() and not stop_number.isdigit():
            lines()
            print("Stop number must contain only numeric values")
        elif  first_number.isdigit() and not multiplier.isdigit() and not stop_number.isdigit():
            lines()
            print("Multiplier number must contain only numeric values")
            print("Stop number must contain only numeric values")
        elif  first_number.isdigit() and not multiplier.isdigit() and stop_number.isdigit():
            lines()
            print("Multiplier number must contain only numeric values")
        elif  not first_number.isdigit() and not multiplier.isdigit() and stop_number.isdigit():
            lines()
            print("First number must contain only numeric values")
            print("Multiplier number must contain only numeric values")
        elif  not first_number.isdigit() and multiplier.isdigit() and stop_number.isdigit():
            lines()
            print("First number must contain only numeric values")
        elif  not first_number.isdigit() and multiplier.isdigit() and not stop_number.isdigit():
            lines()
            print("First number must contain only numeric values")
            print("Stop number must contain only numeric values")
        elif  not first_number.isdigit() and not multiplier.isdigit() and not stop_number.isdigit():
            lines()
            print("First number must contain only numeric values")
            print("Multiplier number must contain only numeric values")
            print("Stop number must contain only numeric values")
        else:
            lines()
            print("Issues with the user input")

    #user input contain only numeric values
    elif first_number.isdigit() and multiplier.isdigit() and stop_number.isdigit():
        ans=int(first_number)*int(multiplier)
        if (int(ans)>int(stop_number)) or (int(ans)>=int(stop_number)):
            if (int(ans)>int(stop_number)):
                lines()
                print(f"{first_number} times {multiplier} --> {ans}")
                print(f"{ans} is greather than {stop_number}")
                print("Nothing can be done")
            elif (int(ans)>=int(stop_number)):
                lines()
                print(f"{first_number} times {multiplier} --> {ans}")
                print(f"{ans} is equal to {stop_number}")
                print("Nothing can be done")
        elif (int(ans)<int(stop_number)):
                  while(int(ans)<int(stop_number)):
                        lines()
                        print(f"{first_number} times {multiplier} --> {ans}")
                        multiplier=int(multiplier)+1
                        ans=int(first_number)*int(multiplier)
                        time.sleep(1)
