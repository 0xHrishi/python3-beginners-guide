#!/usr/bin/python3
#Python3 script 
#2 number from user, add those numbers and check the sum whether its odd or even

f_number=input("Enter the first number:\n")
s_number=input("Enter the second number:\n")


if (len(f_number)<=0) or (len(s_number)<=0):
    if (len(f_number)>0) and (len(s_number)<=0):
        print("*"*20)
        print("Second number field is empty")
    elif (len(f_number)<=0) and (len(s_number)>0):
        print("*"*20)
        print("First number field is empty")
    else:
        print("*"*20)
        print("Issues with the user input")
elif (len(f_number)>0) and (len(s_number)>0):
      sum=int(f_number)+int(s_number)
      if (sum%2==0):
        print ("Sum is " + str(sum))
        print("Sum is even number")
      else:
        print ("Sum is " + str(sum))
        print("Sum is odd number")
