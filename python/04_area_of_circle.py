#!/usr/bin/python

# Description -- Very basic program to calculate the area of the circle using constant

#!/usr/bin/python

# user input 
radius = float(input("Enter the radius of the circle:\n"))

# constant 
PI = 3.14

# formulae to calculate area of circle
area_of_circle = PI * radius * radius

# display the area of circle
print(f"Radius of the circle --> {radius}")
print(f"Area of circle --> {area_of_circle}")
print(f"Area of circle --> {area_of_circle:.2f}")

--------------------------------------------------------------------------------------------------------
#!/usr/bin/python

# function to display lines
def lines():
        print("*"*75)

# user input
radius = input("Enter the radius of the circle:\n")

# constant
PI = 3.14

# check user input
if len(radius) == 0:
        lines()
        print("User input --> Radius field empty")
# user input not empty
# validate user input i.e. must contain only numeric values greater than zero
# validation passed --> calculate area of circle 
else:
        lines()
        if not radius.replace(".","").isdigit():
                print("Radius field must contain positive numeric values")
        else:
                radius = float(radius)
                if radius >= 0:
                        area_of_circle = PI * radius * radius
                        print(f"Radius of the circle --> {radius}")
                        print(f"Area of the circle --> {area_of_circle}")
                        print(f"Area of the circle --> {area_of_circle:.2f}")
                else:
                        print(f"Radius of the circle cannot be less than zero")
