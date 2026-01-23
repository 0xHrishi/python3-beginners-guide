# Variable and constant example 
# This program asks the user to enter the radius of a circle and then calculates the area of circle

# Input: Get radius value from the user
radius = float(input("Enter the radius of the circle\n"))

# Constant value of PI
PI = 3.14
# Calculation: Area of the circle
# area_of_circle = PI * radius ** 2
area_of_circle = PI * radius * radius

# Output: Show radius and calculated area
print(f"Radius of the circle -- {radius}")
print(f"Area of circle -- {area_of_circle}")
print(f"Area of circle (rounded to 2 decimals) -- {area_of_circle:.2f}")

########################################################################################
#!/usr/bin/python
# ------------------------------------------------------------
# Area of a Circle Calculator
# ------------------------------------------------------------
# This script:
# 1. Takes radius input from the user
# 2. Checks for empty input
# 3. Validates numeric input (ignores decimal point)
# 4. Calculates area of a circle
# 5. Prints formatted output
# ------------------------------------------------------------

def lines():
    print("*"*50)

# prompt for user input
radius = input("Enter the radius of the circle:\n")

# constant 
PI=3.14

# User input empty
if len(radius) == 0:
    lines()
    print("User input --> Radius of the circle field is empty")

# Input validation: empty input check, numeric check
# Decimal point is ignored during validation
elif len(radius) > 0:
    lines()
    if not radius.replace(".", "").isdigit():
        print(f"Kindly check the user input")
    elif radius.replace(".", "").isdigit():
        radius = float(radius)
        area_of_circle = PI * radius * radius
        print(f"Radius of the circle --> {radius}")
        print(f"Area of circle --> {area_of_circle}")
        print(f"Area of circle --> {area_of_circle:.2f}")
