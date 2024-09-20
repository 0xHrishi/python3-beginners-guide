#!/usr/bin/python3

#two numbers as user input, use the range function and display only odd numbers

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
            if(int(even_number%2!=0)):
               print("Number is " + str(even_number))
            else:
               even_number=int(even_number)+1
               continue

    else:
        print("First number is greater than second")
        print("Cant do anything")

----------------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

first=input("Enter the first number\n")
second=input("Enter the second number\n")


if (len(first)<=0) or (len(second)<=0):
    if (len(first)>0) and (len(second)<=0):
        print("*"*30)
        print("Second number field is empty")
    elif (len(first)<=0) and (len(second)>0):
        print("*"*30)
        print("First number field is empty")
    elif (len(first)<=0) and (len(second)<=0):
        print("*"*30)
        print("First number field is empty")
        print("Second number field is empty")
    else:
        print("*"*30)
        print("Issues with the user input")
elif (len(first)>0) and (len(second)>0):
    if not first.isdigit() or not second.isdigit():
        if first.isdigit() and not second.isdigit():
            print("*"*30)
            print ("Second number field must contain only nuermic digits")
        elif not first.isdigit() and second.isdigit():
            print("*"*30)
            print ("First number field must contain only nuermic digits")
        elif not first.isdigit() and not second.isdigit():
            print("*"*30)
            print ("First number field must contain only nuermic digits")
            print ("Second number field must contain only nuermic digits")
        else:
            print("*"*30)
            print("Issues with user input validation")
    elif first.isdigit() and second.isdigit():
        print("*"*50)
        option=input("Would you like to print even or odd numbers\n")
        if (str(option)=="even"):
            for even_numbers in range(int(first),int(second)):
                if(int(even_numbers)%2==0):
                    print("*"*20)
                    print("Even numbers is -->" + str(even_numbers))
                else:
                    continue

        elif (str(option)=="odd"):
            for odd_numbers in range(int(first),int(second)):
                if(int(odd_numbers)%2!=0):
                    print("*"*20)
                    print("Odd numbers is -->" + str(odd_numbers))
                else:
                    continue
        else:
            print("*"*50)
            print("Invalid user option")

