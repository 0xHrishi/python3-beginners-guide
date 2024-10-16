#!/usr/bin/python3

#takes two numbers as user input and use the range method to display only even numbers

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
            if(int(even_number%2==0)):
               print("Number is " + str(even_number))
            else:
               even_number=int(even_number)+1
               continue

    else:
        print("First number is greater than second")
        print("Cant do anything")
-----------------------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3


#!/usr/bin/python3

import time

first=input("Enter the first number\n")
second=input("Enter the second number\n")

if len(first)==0 or len(second)==0:
    if len(first)>0 and len(second)==0:
        print("*"*50)
        print("Second number field is empty")
    elif len(first)==0 and len(second)>0:
        print("*"*50)
        print("First number field is empty")
    elif len(first)==0 and len(second)==0:
        print("*"*50)
        print("First number field is empty")
        print("Second number field is empty")
    else:
        print("*"*50)
        print("Issues with the user input")

elif len(first)>0 and len(second)>0:
    if not first.isdigit() or not second.isdigit():
        if first.isdigit() and not second.isdigit():
            print("*"*50)
            print("Second number field must contain only numeric digits")
        elif not first.isdigit() and second.isdigit():
            print("*"*50)
            print("First number field must contain only numeric digits")
        elif not first.isdigit() and not second.isdigit():
            print("*"*50)
            print("First number field must contain only numeric digits")
            print("Second number field must contain only numeric digits")
        else:
            print("*"*50)
            print("Issues with the user input validation")
    elif first.isdigit() and second.isdigit():
        if int(first)<int(second):
            print("*"*50)
            choice=input("Would you like to print even or odd numbers\n")
            if choice=="even":
                for even_numbers in range(int(first),int(second)+1):
                    if int(even_numbers)%2==0:
                        print(f"Even numbers --> {even_numbers}")
                        time.sleep(0.5)
                    else:
                        time.sleep(0.5)
                        continue
            elif choice=="odd":
                for odd_numbers in range(int(first),int(second)+1):
                    if int(odd_numbers)%2!=0:
                        print(f"Odd numbers --> {odd_numbers}")
                        time.sleep(0.5)
                    else:
                        time.sleep(0.5)
                        continue
        elif int(first)==int(second):
            print("*"*50)
            print(f"{first} is equal to {second}")
            print("Cannot do anything")
        elif int(first)>int(second):
            print("*"*50)
            print(f"{first} is greather than {second}")
            print("Cannot do anything")
