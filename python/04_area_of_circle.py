# Variable and constant example 
# This program asks the user to enter the radius of a circle and then calculates the area of circle

# Input: Get radius value from the user
radius = float(input("Enter the radius of the circle\n"))

# Constant value of PI
PI = 3.14
# Calculation: Area of the circle
area_of_circle = PI * radius * radius

# Output: Show radius and calculated area
print(f"Radius of the circle -- {radius}")
print(f"Area of circle -- {area_of_circle}")
print(f"Area of circle (rounded to 2 decimals) -- {area_of_circle:.2f}")
