#!/usr/bin/python3

#two numbers as user input, use the range function and display only odd numbers

first=input("Enter the first number:\n")
second=input("Enter the second number:\n")


if (len(first)<=0) or (len(second)<=0):
    if (len(first)>0) and (len(second)<=0):
        print ("Second number field is empty")
    elif (len(first)<=0) and (len(second)>0):
        print ("First number field is empty")
    else:
        print ("Issues with the user input")


elif(len(first)>0) and (len(second)>0):
    print("*" * 30)
    if (int(first)< int(second)):
        for even_number in range(int(first),int(second)):
            if(int(even_number%2!=0)):
               print("Number is " + str(even_number))
            else:
               even_number=int(even_number)+1
               continue

    else:
        print("First number is greater than second")
        print("Cant do anything")

