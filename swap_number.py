#!/usr/bin/python3
#python3 basic script to swap two numbers.   

f_number=input("Enter the first number:\n")
s_number=input("Enter the second number:\n")

if (len(f_number)<=0) or (len(s_number)<=0):
    if (len(f_number)>0) and (len(s_number)<=0):
        print("Second number field is empty")
    elif(len(f_number)<=0) and (len(s_number)>0):
        print("First number field is empty")
    else:
        print("Issues with the usr input")

elif(len(f_number)>0) and (len(s_number)>0):
    print("*"*30)
    print("Value of first number is: " + str(s_number))
    print("Value of second number is: " + str(f_number))
