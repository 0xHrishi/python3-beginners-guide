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

#!/usr/bin/python3

def user_input():
    global first
    global second
    first=input("Enter the first number\n")
    second=input("Enter the second number\n")

def validation_1():
    if (len(first)==0) or (len(second)==0):
        if (len(first)>0) and (len(second)==0):
            print("*"*30)
            print("Second number field is empty")
            try_again()
        elif (len(first)==0) and (len(second)>0):
            print("*"*30)
            print("First number field is empty")
            try_again()
        elif (len(first)==0) and (len(second)==0):
            print("*"*30)
            print("First number field is empty")
            print("Second number field is empty")
            try_again()
        else:
            print("*"*30)
            print("Issues with the user input")
            try_again()

def validation_2():
    if (len(first)>0) and (len(second)>0):
        if not first.isdigit() or not second.isdigit():
            if first.isdigit() and not second.isdigit():
                print("*"*30)
                print("Second number field must contain only digits")
                try_again()
            elif not first.isdigit() and second.isdigit():
                print("*"*30)
                print("First number field must contain only digits")
                try_again()
            elif not first.isdigit() and not second.isdigit():
                print("*"*30)
                print("First number field must contain only digits")
                print("Second number field must contain only digits")
                try_again()
            else:
                print("*"*30)
                print("Issues with user input validation")
                try_again()

        elif first.isdigit() and second.isdigit():
            print("*"*50)
            print("Press 1 for Addition\n")
            print("Press 2 for Subtraction\n")
            print("Press 3 for Multiply\n")
            print("Press 4 for Power\n")
            choice=input("*******Calculation******\n")
            if (choice=="1"):
                print("*"*40)
                ans=int(first)+int(second)
                print(f"{first} plus {second} --> {ans}")
                try_again()
            elif (choice=="2"):
                print("*"*40)
                ans=int(first)-int(second)
                print(f"{first} minus {second} --> {ans}")
                try_again()
            elif (choice=="3"):
                print("*"*40)
                ans=int(first)*int(second)
                print(f"{first} multiply {second} --> {ans}")
                try_again()
            elif (choice=="4"):
                print("*"*40)
                ans=int(first)**int(second)
                print(f"{first} power {second} --> {ans}")
                try_again()
            else:
                print("*"*40)
                print("Invalid user input")
                try_again()


def try_again():
    again=input("Would you like to try again y/n\n")
    if(again=="y"):
        user_input()
        validation_1()
        validation_2()
    elif(again=="n"):
        print("*"*40)
        print("You choose to quit, bye")
    else:
        print("*"*40)
        print("Invalid user input for try again")





user_input()
validation_1()
validation_2()
