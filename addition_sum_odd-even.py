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
------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

first_number=input("Enter the first number:\n")
second_number=input("Enter the second number:\n")

if (len(first_number)<=0) or (len(second_number)<=0):
    if (len(first_number)>0) and (len(second_number)<=0):
        print("Second number field is empty")
    elif (len(first_number)<=0) and (len(second_number)>0):
        print("First number field is empty")
    else:
        print("Issues with the user input")

elif (len(first_number)>0) and (len(second_number)>0):
    print("*"*40)
    print("First number is " + first_number )
    print("Second number is " + second_number )
    print("*"*40)
    ans=int(first_number)+int(second_number)
    if(ans%2==0):
        print("Addition is " + str(ans))
        print("Result is even number")
    else:
        print("Addition is " + str(ans))
        print("Result is odd number")

