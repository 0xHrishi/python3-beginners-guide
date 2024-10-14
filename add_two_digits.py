#!/usr/bin/python3

number=input("Enter the two digits number\n")

if (len(number)==0):
    print("*"*50)
    print("Number field is empty")
else:
    print("*"*50)
    number_1=str(number[0])
    number_2=str(number[1])
    print(f"First number is {number_1}")
    print(f"Second number is {number_2}")
    ans=int(number_1)+int(number_2)
    print(f"{number_1} plus {number_2} --> {ans}")
