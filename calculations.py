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
