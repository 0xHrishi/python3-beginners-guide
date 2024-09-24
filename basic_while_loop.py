#!/usr/bin/python3
#basic while loop
#first number is multipliy by multiplier which is increase by 1 byevey while loop iteration and stop when the result reached is equal to stop number

import time


f_number=input("Enter the first number\n")
multiplier=input("Enter the multiplier number\n")
stop_number=input("Enter the stop number\n")

if (len(f_number)<=0) or (len(multiplier)<=0) or (len(stop_number)<=0):
    if (len(f_number)>0) and (len(multiplier)>0) and (len(stop_number)<=0):
        print("*"*40)
        print("Stop number field is empty")
    elif (len(f_number)>0) and (len(multiplier)<=0) and (len(stop_number)<=0):
        print("*"*40)
        print("Multiplier field is empty")
        print("Stop number field is empty")
    elif (len(f_number)>0) and (len(multiplier)<=0) and (len(stop_number)>0):
        print("*"*40)
        print("Multiplier field is empty")
    elif (len(f_number)<=0) and (len(multiplier)>0) and (len(stop_number)<=0):
        print("*"*40)
        print("First number field is empty")
        print("Stop number field is empty")
    elif (len(f_number)<=0) and (len(multiplier)<=0) and (len(stop_number)>0):
        print("*"*40)
        print("First number field is empty")
        print("Multiplier number field is empty")
    elif (len(f_number)<=0) and (len(multiplier)<=0) and (len(stop_number)<=0):
        print("*"*40)
        print("First number field is empty")
        print("Multiplier field is empty")
        print("Stop number field is empty")
elif (len(f_number)>0) and (len(multiplier)>0) and (len(stop_number)>0):
    print("*"*40)
    ans=int(f_number)*int(multiplier)
    if(int(ans) < int(stop_number)):
        while (int(ans) < int(stop_number)):
            print (str(f_number) + " times " + str(multiplier) + " is " + str(ans))
            multiplier=int(multiplier)+1
            ans=int(f_number)*int(multiplier)
            time.sleep(0.3)

    elif(int(ans) >= int(stop_number)):
        print(str(ans) + " is greather than " + str(stop_number))
        print("Nothing to do")
    else:
        print("Something went wrong")
-----------------------------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

#!/usr/bin/python3

import time

first=input("Enter the first number:\n")
multiplier=input("Enter the multiplier number:\n")
stop_number=input("Enter the stop number:\n")

if (len(first)==0) or (len(multiplier)==0) or (len(stop_number)==0):
    if (len(first)>0) and (len(multiplier)==0) and (len(stop_number)==0):
        print("*"*30)
        print("Multiplier number field is empty")
        print("Stop number field is empty")
    elif (len(first)>0) and (len(multiplier)>0) and (len(stop_number)==0):
        print("*"*30)
        print("Stop number field is empty")
    elif (len(first)>0) and (len(multiplier)==0) and (len(stop_number)>0):
        print("*"*30)
        print("Multiplier number field is empty")
    elif (len(first)==0) and (len(multiplier)>0) and (len(stop_number)>0):
        print("*"*30)
        print("First number field is empty")
    elif (len(first)==0) and (len(multiplier)==0) and (len(stop_number)>0):
        print("*"*30)
        print("First number field is empty")
        print("Multiplier number field is empty")
    elif (len(first)==0) and (len(multiplier)>0) and (len(stop_number)==0):
        print("*"*30)
        print("First number field is empty")
        print("Stop number field is empty")
    elif (len(first)==0) and (len(multiplier)==0) and (len(stop_number)==0):
        print("*"*30)
        print("First number field is empty")
        print("Multiplier number field is empty")
        print("Stop number field is empty")
    else:
        print("*"*30)
        print("Issues with the user input")
elif (len(first)>0) and (len(multiplier)>0) and (len(stop_number)>0):
    if not first.isdigit() or not multiplier.isdigit() or not stop_number.isdigit():
        if first.isdigit() and not multiplier.isdigit() and not stop_number.isdigit():
            print("*"*30)
            print("Mutiplier number field must contain only digits")
            print("Stop number field must contain only digits")
        elif first.isdigit() and multiplier.isdigit() and not stop_number.isdigit():
            print("*"*30)
            print("Stop number field must contain only digits")
        elif first.isdigit() and not multiplier.isdigit() and stop_number.isdigit():
            print("*"*30)
            print("Multiplier number field must contain only digits")
        elif not first.isdigit() and multiplier.isdigit() and stop_number.isdigit():
            print("*"*30)
            print("First number field must contain only digits")
        elif not first.isdigit() and not multiplier.isdigit() and stop_number.isdigit():
            print("*"*30)
            print("First number field must contain only digits")
            print("Multiplier number field must contain only digits")
        elif not first.isdigit() and multiplier.isdigit() and not stop_number.isdigit():
            print("*"*30)
            print("First number field must contain only digits")
            print("Stop number field must contain only digits")
        elif not first.isdigit() and not multiplier.isdigit() and not stop_number.isdigit():
            print("*"*30)
            print("First number field must contain only digits")
            print("Multiplier number field must contain only digits")
            print("Stop number field must contain only digits")
        else:
            print("*"*30)
            print("Issues with user input validation")
    elif first.isdigit() and multiplier.isdigit() and  stop_number.isdigit():
        ans=int(first)*int(multiplier)
        if(int(ans)<int(stop_number)):
            while(int(ans)<int(stop_number)):
                print(f"{first} times {multiplier} --> {ans}")
                multiplier=int(multiplier)+1
                ans=int(first)*int(multiplier)
                time.sleep(1)
        elif(int(ans)==int(stop_number)):
            print("*"*30)
            print(f"{first} times {multiplier} --> {ans}")
            print(f"{ans} is equal to {stop_number}")
            print("Nothing can be done")
        elif(int(ans)>int(stop_number)):
            print("*"*30)
            print(f"{first} times {multiplier} --> {ans}")
            print(f"{ans} is greater than {stop_number}")
            print("Nothing can be done")

