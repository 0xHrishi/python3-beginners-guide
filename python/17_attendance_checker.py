#!/usr/bin/python
# Accepts total classes and classes attended from user
# Calculates attendance percentage
# Provides eligibility messages based on attendance

# Function to print a line
def lines():
        print("*"*100)

# Prompt user input
total_class = input("Enter the total number of classes held:\n")
attend_class = input("Enter the total number of classes attended:\n")

# User input empty
if len(total_class) == 0 or len(attend_class) == 0:
        lines()
        if len(total_class) == 0:
                print("User input --> Total number of classes field is empty")
        if len(attend_class) == 0:
                print("User input --> Number of class attended field is empty")

# If user input not empty
# Validation check -- user input contain only numeric values
# Convert inputs to integers
# Calculate attendance percentage and print eligiblity messages
elif len(total_class) > 0 and len(attend_class) > 0:
        lines()
        if not total_class.isdigit() or not attend_class.isdigit():
                if not total_class.isdigit():
                        print("Total number of classes held field must contain only numeric values")
                if not attend_class.isdigit():
                        print("Total number of classes attended field must contain only numeric values")
        elif total_class.isdigit() and attend_class.isdigit():
                total_class = int(total_class)
                attend_class = int(attend_class)

                lines
                if attend_class > total_class:
                        print("Number of class attended cannot be greater than number of class held")
                elif attend_class == total_class or attend_class <= total_class:
                        attendance_percentage = ( attend_class / total_class ) * 100
                        if attendance_percentage >= 75:
                                print(f"Number of classes held --> {total_class}")
                                print(f"Number of classes attended --> {attend_class}")
                                print(f"Attendance percentage --> {attendance_percentage:.2f}")
                                print("You are eligible for writing the exam")
                        elif attendance_percentage >= 65 and attendance_percentage <= 74:
                                print(f"Number of classes held --> {total_class}")
                                print(f"Number of classes attended --> {attend_class}")
                                print(f"Attendance percentage --> {attendance_percentage:.2f}")
                                print("Percentage low -- but can be improved")
                        elif attendance_percentage <= 64:
                                print(f"Number of classes held --> {total_class}")
                                print(f"Number of classes attended --> {attend_class}")
                                print(f"Attendance percentage --> {attendance_percentage:.2f}")
                                print("Contact principal")
