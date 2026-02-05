# ------------------------------------------------------------
# Program: Demonstrate Local vs Global Variables in Python
# ------------------------------------------------------------
#!/usr/bin/python

number_1 = 10

def global_variable():
    global number_1
    number_1 = 20
    print(f"Value of number within the function -- > {number_1}")



print("**********Global variable example**********")
print(f"Value of number before the function called -- > {number_1}")
global_variable()
print(f"Value of number After the function called -- > {number_1}")

#**********Global variable example**********
# Value of number before the function called -- > 10
# Value of number within the function -- > 20
# Value of number After the function called -- > 20
#**********Global variable example**********
number_2 = 100

def local_variable():
    number_2 = 200
    print(f"Value of number within the function -- > {number_2}")

print("**********Global variable example**********")
print(f"Value of number before the function called -- > {number_2}")
local_variable()
print(f"Value of number after the function called -- > {number_2}")
#**********Local variable example**********
# Value of number before the function called -- > 100
# Value of number within the function -- > 200
# Value of number after the function called -- > 100
#**********Local variable example**********
