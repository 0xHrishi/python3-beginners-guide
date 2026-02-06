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
#!/usr/bin/python
# calculate area of circle 
def lines():
    print("*"*75)

# prompt user input
radius = input("Enter the radius of the circle\n")

# user input empty
if len(radius) == 0:
    lines()
    print(f"User input --> Radius of the circle field is empty")

# user input not empty
# validation check i.e. user input must be positive numeric value
else:
    lines()
    if not radius.replace(".", "").isdigit():
        print("Radius of circle field must contain only positive numeric values")
    if radius.replace(".", "").isdigit():
        radius = float(radius)
        if radius == 0:
            print(f"Radius of the circle cannot be zero")
        elif radius < 0:
            print(f"Radius of the circle cannot be less than zero")
        else:
            PI = 3.14
            area_of_circle = PI * radius ** 2
            print(f"Radius of circle {radius}")
            print(f"Area of circle {area_of_circle:.2f}")
