# ------------------------------------------------------------
# Program: Calculate the Area of a Circle
# Description:
#     This program takes the radius of a circle as input from the user
#     and calculates the area using the formula:
#         Area = 3.14 × radius * radius
# ------------------------------------------------------------

# Ask the user to enter the radius and convert it to float
radius = float(input("Enter the radius of the circle\n"))

# PI -- constant 
PI=3.14

# Calculate the area of the circle using the formula
area_of_circle = PI * (radius*radius)

# Print the radius entered by the user
print(f"Radius of the circle : {radius}")
# Print the full area without rounding
print(f"Area of circle --> {area_of_circle}")
# Print the full area without rounding
print(f"Area of circle --> {area_of_circle:.2f}")
