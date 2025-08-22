#functions

#def means define, welcome() --> function name
#Non parameterized functions
def welcome():
    print("Welcome")

#call the function
welcome()
welcome()


#Parameterized functions
#Arguments

def add(first,second):
    sum=first+second
    print(f"{first} plus {second} --> {sum}")

add(15,30)

#Paramters
def addition(first_number,second_number):
    result=first_number+second_number
    print(f"{first_number} plus {second_number} --> {result}")

first=int(input("Enter first number:\n"))
second=int(input("Enter the second number"))

addition(first,second)
