# ------------------------------------------------------------
# Program: Demonstrate Local vs Global Variables in Python
# ------------------------------------------------------------
#!/usr/bin/python
# Local variable 
def lines():
    print("*"*100)

# variable
number = 10

# function 
def local_variable_ex():
    number = 20
    print(f"Within the function, value of number: {number}")

print(f"Before the function is called, value of number: {number}")
local_variable_ex()
print(f"After the function is called, value of number: {number}")

###########################OUTPUT#################################
# Before the function is called, value of number: 10
# Within the function, value of number: 20
# After the function is called, value of number: 10
##################################################################
# global variable example
lines()

number = 50

def global_variable_ex():
    global number
    number = 100
    print(f"Within the function, value of number: {number}")


print(f"Before the function is called, value of number: {number}")
global_variable_ex()
print(f"After the function is called, value of number: {number}")

###########################OUTPUT#################################
# Before the function is called, value of number: 50
# Within the function, value of number: 100
# After the function is called, value of number: 100
##################################################################
