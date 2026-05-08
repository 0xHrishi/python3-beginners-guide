#!/usr/bin/python

# Basic program to understand the different between global vs local variable 

# variable
num_1 = 10

# function 
# global variable 
def global_variable():
        global num_1
        num_1 = 20
        print(f"Within the function, value of num_1 is {num_1}")

# output
print("*"*50)
print(f"Before the function called, value of num_1 is {num_1}")
global_variable()
print(f"After the function called, value of num_1 is {num_1}")

########################################################################################
################## PROGRAM OUTPUT ###############################
#Before the function called, value of num_1 is 10
#Within the function, value of num_1 is 20
#After the function called, value of num_1 is 20

########################################################################################
print("*"*50)
# variable
# local variable 
num_2 = 20

# function
# local variable 
def local_variable():
        num_2 = 30
        print(f"Within the function, value of num_2 is {num_2}")

print(f"Before the function called, value of num_2 is {num_2}")
local_variable()
print(f"After the function called, value of num_2 is {num_2}")

########################################################################################
################## PROGRAM OUTPUT ###############################
Before the function called, value of num_2 is 20
Within the function, value of num_2 is 30
After the function called, value of num_2 is 20
