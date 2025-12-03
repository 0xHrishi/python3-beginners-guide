# ------------------------------------------------------------
# Program: Demonstrate Local vs Global Variables in Python
# ------------------------------------------------------------

# Global variable example
number = 10

# Created a function i.e. global_example
# And within the function used the global keyword to change the value of the number 
def global_example():
    global number
    number = 20
    print(f"Within the function, the value of number is -- {number}")

print(f"Before the function is called, the value of number is -- {number}")
global_example()
print(f"Function finishes it execution, the value of number is -- {number}")

print("*"*100)

# Local variable example
number = 10

# Created a function i.e. local_example
# And within the function created a local variable (only exists inside the function)
def local_example():
    number = 20
    print(f"Within the function, the value of number is -- {number}")

print(f"Before the function is called, the value of number is -- {number}")
local_example()
print(f"Function finishes it execution -- value of number is -- {number}")

# ----------------------------OUTPUT----------------------------------
# Before the function is called, the value of number is -- 10
# Within the function, the value of number is -- 20
# Function finishes it execution, the value of number is -- 20
# ****************************************************************************************************
# Before the function is called, the value of number is -- 10
# Within the function, the value of number is -- 20
# Function finishes it execution -- value of number is -- 10
