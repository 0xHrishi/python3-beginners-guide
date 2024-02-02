#!/usr/bin/python3
#python3 basic script to add two digit. Two digit from the user input

number=input("Enter a two digit number:\n")

if (len(number)<=0):
    print("Isssues with the user input")
else:
    print("*"*30)
    a=number[0]
    b=number[1]
    sum=int(a)+int(b)
    print("Sum of two digits is: " + str(sum))
