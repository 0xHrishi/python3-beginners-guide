# ------------------------------------------------------------
# Program: Demonstrate Local vs Global Variables in Python
# Description:
#     This program demonstrates how Python handles variable scope.
#     It shows the difference between:
#         1. Local variables (defined inside a function)
#         2. Global variables (declared outside or using 'global' keyword)
# ------------------------------------------------------------

# Example 1: Local Variable

#Gloval variable i.e. number_1
number_1 = 10 

def numbers_1():
    # Local variable (only exists inside this function)
    number_1 = 20
    print(f"Within the function --> Value of number is {number_1}")

# Call the function
numbers_1()

# The global variable 'number_1' remains unchanged
print(f"Outside the function --> Value of number is {number_1}")

 # Separator for clarity
print("*" * 50)


# Example 2: Global Variable
# global keyword --  tells Python to use the global variable as it Modifies the global variable
number_2 = 30  
def numbers_2():
    global number_2  
    number_2 = 40  
    print(f"Within the function --> Value of number is {number_2}")

# Call the function
numbers_2()

# The global variable 'number_2' has been updated by the function
print(f"Outside the function --> Value of number is {number_2}")

# ------------------------------------------------------------
# 🧠 OUTPUT EXAMPLE:
# Within the function --> Value of number is 20
# Outside the function --> Value of number is 10
# **************************************************
# Within the function --> Value of number is 40
# Outside the function --> Value of number is 40
# ------------------------------------------------------------
