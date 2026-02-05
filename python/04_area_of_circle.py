#!/usr/bin/python

# Description -- Very basic program to calculate the area of the circle

# Function 
def lines():
    print("*"*75)

# Prompt user input to enter the radius of the circle
radius = float(input("Enter the radius of the circle\n"))

# PI --> Constant and the value must not be changed
PI = 3.14
# Formulae to calculate area of circle
area_of_circle = PI * radius * radius

lines()
# Display radius and area of circle
print(f"Radius of the circle --> {radius}")
print(f"Area of the circle --> {area_of_circle}")
# Rounding off to 2 decimal 
print(f"Area of the circle --> {area_of_circle:.2f}")

--------------------------------------------------------------------------------------------------------
