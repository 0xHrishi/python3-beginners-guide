#!/usr/bin/python

# function to print lines
def lines():
    print("*"*100)

# user input prompt
total_classes = input("Enter the total number of classes:\n")
attended_classes = input("Enter the number of classes attended:\n")

# if user input is empty
if len(total_classes) == 0 or len(attended_classes) == 0:
    lines()
    if len(total_classes) == 0:
        print("User input --> Total number of classes field is empty")
    if len(attended_classes) == 0:
        print("User input --> Number of classes attended field is empty")

# user iput is not empty
# validate user input i.e. must be an integer value
# validattion passed, calculate the attendance %
else:
    if not total_classes.isdigit() or not attended_classes.isdigit():
        lines()
        if not total_classes.isdigit():
            print("Total number of classes field must contain only integer values")
        if not attended_classes.isdigit():
            print("Number of classes attended field must contain only integer values")

    else:
        total_classes, attended_classes = float(total_classes), float(attended_classes)
        attendance = ( attended_classes / total_classes ) * 100

        lines()
        if total_classes >= attended_classes:
            print(f"Total number of classes --> {int(total_classes)}")
            print(f"Number of classes attended--> {int(attended_classes)}")
            if attendance >= 75:
                print(f"Attendance percentage --> {attendance:.2f}")
            if attendance >= 60 and attendance <=74:
                print(f"Attendance percentage --> {attendance:.2f}")
                print(f"Be careful")
            if attendance >= 0 and attendance <= 59 :
                print(f"Attendance percentage --> {attendance:.2f}")
                print(f"Contact princial")
        else:
            print(f"Total number of classes cannot be greater than number of classes attended")
