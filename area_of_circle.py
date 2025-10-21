# ------------------------------------------------------------
# Program: Calculate the Area of a Circle
# Description:
#     This program takes the radius of a circle as input from the user
#     and calculates the area using the formula:
#         Area = 3.14 × radius * radius
# ------------------------------------------------------------

#Ask the user to enter the radius of the circle
#created a variable named radius
radius = int(input("Enter the radius of the circle: "))

#constant 
PI = 3.14 

# Calculate the area using the formula: π × r²
area_of_circle = PI * radius * radius

print(f"Area of circle --> {area_of_circle:}")

#Display the result, formatted to 2 decimal places
print(f"Area of circle --> {area_of_circle:.2f}")
