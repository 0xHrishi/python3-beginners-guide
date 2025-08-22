#functions
#non parameterized

print("*"*50 + "Non parameterized" + "*"*50)
def welcome ():
    print("Welcome")

welcome()
welcome()

#paramterized
#Arguments
print("*"*50 + "Parameterized --> Arguments" + "*"*50)

def addition(first_number,second_number):
    sum=first_number+second_number
    print(f"First number:{first_number} plus Second number:{second_number} --> {sum}")

addition(15,20)

# Arguments
#User input variable and parameters value can be of same name or different
#for learners same name is ok, but in real projects, different names
print("*" * 50 + "Parameterized --> Parameters" + "*" * 50)

first_number=int(input("Enter the first number\n"))
second_number=int(input("Enter the second number\n"))

def addition(first_number, second_number):
    sum = first_number + second_number
    print(f"First number:{first_number} plus Second number:{second_number} --> {sum}")

addition(first_number,second_number)

# Parameterized - Return
print("*" * 50 + "Parameterized --> Return value" + "*" * 50)

first_number=int(input("Enter the first number\n"))
second_number=int(input("Enter the second number\n"))

def addition(first_number, second_number):
    return first_number + second_number

sum=addition(first_number,second_number)
print(f"{first_number} plus {second_number} --> {sum}")

#lambda
print("*" * 50 + "Parameterized -->  Lambda" + "*" * 50)

first_number=int(input("Enter the first number\n"))
second_number=int(input("Enter the second number\n"))

sum=(lambda first_number,second_number:first_number+second_number)(first_number,second_number)
print(f"{first_number} plus {second_number} --> {sum}")
