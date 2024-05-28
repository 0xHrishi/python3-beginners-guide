#!/usr/bin/python3
#Python3 script 
#2 number from user, add those numbers and check the sum whether its odd or even

#!/usr/bin/python3

f_number=input("Enter the first number -->\n")
s_number=input("Enter the second number -->\n")

if (len(f_number)<=0) or (len(s_number)<=0):
    if (len(f_number)>0) and (len(s_number)<=0):
        print("*"*40)
        print("Second number field is empty")
    elif (len(f_number)<=0) and (len(s_number)>0):
        print("*"*40)
        print("First number field is empty")
    elif (len(f_number)<=0) and (len(s_number)<=0):
        print("*"*40)
        print("User input field is missing")
    else:
        print("*"*40)
        print("Something went wrong")

elif (len(f_number)>0) and (len(s_number)>0):
        print("*"*40)
        print("First number is -->" + f_number)
        print("Second number is -->" + s_number)
        ans=int(f_number)+int(s_number)
        if (int(ans%2==0)):
            print("Additon of " + f_number + " and " + s_number + " is " + str(ans))
            print("Result is even number")
        elif (int(ans%2!=0)):
            print("Additon of " + f_number + " and " + s_number +  " is " + str(ans))
            print("Result is odd number")
        else:
            print("SOmething went wrong")

