#basic calculations 
#user input --> Additon, subtraction, multiplications 

#!/usr/bin/python3

f_number=input("Enter the first number --> \n")
s_number=input("Enter the second number --> \n")

if (len(f_number)<=0) or (len(s_number)<=0):
    if (len(f_number)>0) and (len(s_number)<=0):
        print("*"*20)
        print("Second number field is empty")
    elif (len(f_number)<=0) and (len(s_number)>0):
        print("*"*20)
        print("First number field is empty")
    elif (len(f_number)<=0) and (len(s_number)<=0):
        print("*"*20)
        print("First number field is empty")
        print("Second number field is empty")
    else:
        print("Issues with the user input")
elif (len(f_number)>0) and (len(s_number)>0):
    print("*"*40)
    print("Press 1 --> Addition")
    print("Press 2--> Subtraction")
    print("Press 3 --> Multiplication")
    choice=input("Enter your choice -->")
    if(str(choice) == "1" ):
        print("*"*40)
        ans=int(f_number)+int(s_number)
        print("Addition result is --> " + str(ans) )
    elif(str(choice) == "2" ):
        print("*"*40)
        ans=int(f_number)-int(s_number)
        print("Subtraction result is --> " + str(ans) )
    elif(str(choice) == "3" ):
        print("*"*40)
        ans=int(f_number)*int(s_number)
        print("Multiplication result is --> " + str(ans) )
    else:
        print("Invalid choice")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3
#with functions

def user_input():
    global first
    global second
    first=input("Enter the first number\n")
    second=input("Enter the second number\n")

def user_validation_1():
    if (len(first)<=0) or (len(second)<=0):
        if (len(first)>0) and (len(second)<=0):
            print("*"*50)
            print("Second number field is empty")
            try_again()
        elif (len(first)<=0) and (len(second)>0):
            print("*"*50)
            print("First number field is empty")
            try_again()
        elif (len(first)<=0) and (len(second)<=0):
            print("*"*50)
            print("First number field is empty")
            print("Second number field is empty")
            try_again()
        else:
            print("*"*50)
            print("Issues with the user input")
            try_again()

def user_validation_2():
    if (len(first)>0) and (len(second)>0):
        if not first.isdigit() or not second.isdigit():
            if first.isdigit() and not second.isdigit():
                print("*"*50)
                print("Second number field must contain only numeric digits")
                try_again()
            elif not first.isdigit() and second.isdigit():
                print("*"*50)
                print("First number field must contain only numeric digits")
                try_again()
            elif not first.isdigit() and not second.isdigit():
                print("*"*50)
                print("First number field must contain only numeric digits")
                print("Second number field must contain only numeric digits")
                try_again()
            else:
                print("*"*50)
                print("Issues with the user input validation")
                try_again()
        elif first.isdigit() and second.isdigit():
            print("*"*50)
            print("Press 1 for Addition")
            print("Press 2 for Subtraction")
            print("Press 3 for Multiply")
            print("Press 4 for Power")
            calc=input("******Calculation*******\n")
            if(calc == "1"):
                print("*"*50)
                ans=int(first)+int(second)
                print(f"{first} plus {second} is {ans}")
                try_again()
            elif(calc == "2"):
                print("*"*50)
                ans=int(first)-int(second)
                print(f"{first} minus {second} is {ans}")
                try_again()
            elif(calc == "3"):
                print("*"*50)
                ans=int(first)*int(second)
                print(f"{first} multiply {second} is {ans}")
                try_again()
            elif(calc == "4"):
                print("*"*50)
                ans=int(first)**int(second)
                print(f"{first} power {second} is {ans}")
                try_again()
            else:
                print("*"*50)
                print("Invalid user input")
                try_again()

def try_again():
    print("*"*50)
    choice=input("Would you like to try again y/n?\n")
    if(choice=="y"):
        print("*"*50)
        user_input()
        user_validation_1()
        user_validation_2()
    elif(choice=="n"):
        print("*"*50)
        print("You choose to quit")
    else:
        print("*"*50)
        print("Invalid user choice")



user_input()
user_validation_1()
user_validation_2()

