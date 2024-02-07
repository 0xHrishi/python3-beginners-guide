#!/usr/bin/python3

first=input("Enter the first number:\n")
multiply=input("Enter the multiply number:\n")
stop_number=input("Enter the stop number:\n")


if (len(first)<=0) or (len(multiply)<=0) or (len(stop_number)<=0):
    if (len(first)>0) and (len(multiply)<=0) and (len(stop_number)<=0):
        print("*" * 20)
        print ("Multiplier number is empty")
        print ("Stop number is empty")
    elif (len(first)>0) and (len(multiply)>0) and (len(stop_number)<=0):
        print("*" * 20)
        print ("Stop number is empty")
    elif (len(first)>0) and (len(multiply)<=0) and (len(stop_number)>0):
        print("*" * 20)
        print ("Multiplier number is empty")
    elif (len(first)<=0) and (len(multiply)>0) and (len(stop_number)<=0):
        print("*" * 20)
        print ("First number is empty")
        print ("Stop number is empty")
    elif (len(first)>0) and (len(multiply)>0) and (len(stop_number)<=0):
        print("*" * 20)
        print ("Stop number is empty")
    elif (len(first)<=0) and (len(multiply)>0) and (len(stop_number)>0):
        print("*" * 20)
        print ("First number is empty")
    elif (len(first)<=0) and (len(multiply)<=0) and (len(stop_number)>0):
        print("*" * 20)
        print ("First number is empty")
        print ("Multiplier number is empty")
    else:
        print ("issues with the user input")
elif(len(first)>0) and (len(multiply)>0) and (len(stop_number)>0):
    print ("*"* 20)
    ans=int(first)*int(multiply)
    if(int(ans)<int(stop_number)):
       while(int(ans)<int(stop_number)):
            ans=int(first)*int(multiply)
            print(f"{first} times {multiply} is {ans}")
            multiply=int(multiply)+1
            ans=int(first)*int(multiply)

    else:
       print(f"{ans} is greater than {stop_number}")
       print("Can't go futher")
