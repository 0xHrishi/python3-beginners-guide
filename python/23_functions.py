
# NON PARAMETERIZED FUNCTIONS
# does not take input from the user
def lines():
    print("*"*100)

lines()

# PARAMETERIZED FUNCTIONS -- PARAMETERS
# Takes different values
first_number = int(input("Enter the first number\n"))
second_number = int(input("Enter the second number\n"))

def add(number_1, number_2):
    sum = number_1 + number_2
    print(f"{number_1} plus {number_2} -- {sum}")

add(first_number, second_number)


# PARAMETERIZED FUNCTIONS -- ARGUMENTS
# Values are fixed
def subtract(number_3, number_4):
    sub = number_3 - number_4
    print(f"{number_3} plus {number_4} -- {sub}")

subtract(100,20)

# LAMDA FUNCTIONS 
# GOOD FOR SHORT TERM 
first_number = int(input("Enter first number\n"))
second_number = int(input("Enter second number\n"))

add = (lambda num_1,num_2: num_1 + num_2)(first_number, second_number)

print(f"{add}")
