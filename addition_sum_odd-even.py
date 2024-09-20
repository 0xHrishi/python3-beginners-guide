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
------------------------------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

first=input("Enter the first number\n")
second=input("Enter the second number\n")


if (len(first)<=0) or (len(second)<=0):
    if (len(first)>0) and (len(second)<=0):
        print ("*"*20)
        print("Second number field is empty")
    elif (len(first)<=0) and (len(second)>0):
        print ("*"*20)
        print("First number field is empty")
    elif (len(first)<=0) and (len(second)<=0):
        print ("*"*20)
        print("First number field is empty")
        print("Second number field is empty")
    else:
        print ("*"*20)
        print("Issues with the user input")


elif (len(first)>0) and (len(second)>0):
    if not first.isdigit() or not second.isdigit():
        if first.isdigit() and not second.isdigit():
            print ("*"*20)
            print ("Second number field must contain only numeric digits")
        elif not first.isdigit() and second.isdigit():
            print ("*"*20)
            print ("First number field must contain only numeric digits")
        elif not first.isdigit() and not second.isdigit():
            print ("*"*20)
            print ("First number field must contain only numeric digits")
            print ("Second number field must contain only numeric digits")
        else:
            print ("*"*20)
            print("Issues with the user input validation")
    elif first.isdigit() and second.isdigit():
        ans=int(first)+int(second)
        if (int(ans)%2==0):
            print ("*"*20)
            print(str(first) + " plus " + str(second) + " is " + str(ans))
            print("Result is an " + str(ans) + " even number")
        elif (int(ans)%2!=0):
            print ("*"*20)
            print(str(first) + " plus " + str(second) + " is " + str(ans))
            print("Result is an " + str(ans) + " odd number")
        else:
            print ("*"*20)
            print ("Issues with calculation")


