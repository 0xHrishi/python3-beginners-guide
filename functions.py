#functions
#non parameterized

#def --> Define a function and function name
print("*" *50 + "Non parameterized functions" + "*" * 50)
def welcome():
    print("Welcome")

#Call a function
welcome()
welcome()

#Parameterized functions
#Arguments
print("*" *50 + "Parameterized functions -- Arguments" + "*" * 50)

def add(first_number,second_number):
    sum=first_number+second_number
    print(f"First number:{first_number} plus Second number:{second_number} --> {sum}")

add(50,30)

#Parameterized functions
#Parameters
print("*" *50 + "Parameterized functions -- Parameters" + "*" * 50)
first_number=int(input("Enter first number\n"))
second_number=int(input("Enter second number\n"))

def add(number_1,number_2):
    sum=number_1+number_2
    print(f"First number:{number_1} plus Second number:{second_number} --> {sum}")

add(first_number,second_number)

#Parameterized functions
#Return
print("*" *50 + "Parameterized functions -- Return" + "*" * 50)
first_number=int(input("Enter first number\n"))
second_number=int(input("Enter second number\n"))

def add(number_1,number_2):
    return number_1+number_2

result=add(first_number,second_number)
print(f"{result}")

#lambda
#use for small task
print("*" *50 + "Lambda" + "*" * 50)
first_number=int(input("Enter first number\n"))
second_number=int(input("Enter second number\n"))

result=(lambda first_number,second_number:first_number+second_number)(first_number,second_number)
print(f"{result}")


