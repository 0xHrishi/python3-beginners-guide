#variable first_number
first_number=10

#defined a function called numbers
#global variable: first_number
def numbers ():
    global first_number
    first_number=20

    #local variable which can be used within the function
    #If used outside the function, python will display an error
    second_number=20
    print(f"Value of second number within function --> {second_number}")

#value of first number will be 10, why becuase the function has not been called
print(f"First number before function called --> {first_number}")
#function called
numbers()
#value of first number changes from 10 to 20. 
print(f"First number after function called -> {first_number}")
