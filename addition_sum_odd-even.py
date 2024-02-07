#!/usr/bin/python3
#Python3 script 
#2 number from user, add those numbers and check the sum whether its odd or even

first=input("Enter the first number:\n")
second=input("Enter the second number:\n")


if (len(first)<=0) or (len(second)<=0):
    if (len(first)>0) and (len(second)<=0):
        print("Second number field is empty")
    elif (len(first)<=0) and (len(second)>0):
        print("First number field is empty")
    else:
        print("Issues with the user input")

elif(len(first)>0) and (len(second)>0):
    print("*" * 20)
    print(f"First number is --> {first}")
    print(f"second number is --> {second}")
    print("*" * 20)
    ans=int(first)+int(second)
    if (int(ans)%2==0):
        print(f"{first} plus {second} is --> {ans}")
        print("Sum is even number")
    else:
        print(f"{first} plus {second} is --> {ans}")
        print("Sum is odd number")
