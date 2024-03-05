#!/usr/bin/python3


lbs=input("Enter your weight in lbs:\n")

if (len(lbs)<=0):
    print("lbs field empty")
else:
    print("*"*30)
    kg=0.454*float(lbs)
    print("Your weight in lbs is " + str(lbs))
    print("Your weight in kg is " + str(kg))
    print("*"*30)
