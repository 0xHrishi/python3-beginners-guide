#!/usr/bin/python3

print("************Guess Game *************")
number=input("Enter the number:\n")

if(len(number)<=0):
    print("Number field is empty")
else:
    count=0
    guess_number=3
    while (count<=3):
        if (int(number)==int(guess_number)):
            print("You guess correct number")
            break
        else:
            count=int(count+1)
            print("Incorrect guess, try gain")
            number=input("Enter the number:\n")
            continue
