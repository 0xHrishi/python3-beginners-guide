#!/usr/bin/python3

first_number=input("Enter first number\n")
second_number=input("Enter second number\n")
stop_number=input("Enter stop number\n")


if (len(first_number)<=0) or (len(second_number)<=0) or (len(stop_number)<=0):
    if (len(first_number)>0) and (len(second_number)>0) and (len(stop_number)<=0):
        print("Stop number field is empty")
    elif (len(first_number)>0) and (len(second_number)<=0) and (len(stop_number)<=0):
        print("Second number field is empty")
        print("Stop number field is empty")
    elif (len(first_number)>0) and (len(second_number)<=0) and (len(stop_number)>0):
        print("Second number field is empty")
    elif (len(first_number)<=0) and (len(second_number)>0) and (len(stop_number)<=0):
        print("First number field is empty")
        print("Stop number field is empty")
    elif (len(first_number)>0) and (len(second_number)>0) and (len(stop_number)<=0):
        print("Stop number field is empty")
    elif (len(first_number)<=0) and (len(second_number)>0) and (len(stop_number)>0):
        print("First number field is empty")
    elif (len(first_number)<=0) and (len(second_number)<=0) and (len(stop_number)>0):
        print("First number field is empty")
        print("Seoond number field is empty")
    else:
        print("Issues with the user input")

elif (len(first_number)>0) and (len(second_number)>0) and (len(stop_number)>0):
   ans=int(first_number)*int(second_number) 
   if(int(stop_number) > int(ans)):
       while (int(stop_number) > int(ans)):
           ans=int(first_number)*int(second_number)
           print(f"{first_number} times {second_number} is {ans}")
           second_number=int(second_number)+1
           ans=int(first_number)*int(second_number)
   else:
       print(f"{first_number} times {second_number} is {ans}")
       print(f"{ans} is greater than {stop_number} ")
       print("Nothing to do")
