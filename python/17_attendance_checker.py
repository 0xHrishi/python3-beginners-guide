# ---------------------------------------------------------------
# This Python script calculates a student's attendance percentage
# based on total classes and classes attended.
# It performs validation for empty input and numeric input only.
# Depending on the attendance percentage, it provides eligibility
# status for writing exams.
# ---------------------------------------------------------------

def lines():
    print("*"*100)

# Prompt the user for input
total_class = input("Enter the total number of classes\n")
class_attend = input("Enter the number of classes attended\n")

# If user input is empty
if len(total_class) == 0 or len(class_attend) == 0:
    if len(total_class) > 0 and len(class_attend) == 0:
        lines()
        print("User input --> Class attended field is empty")
    elif len(total_class) == 0 and len(class_attend) > 0:
        lines()
        print("User input --> Total classes field is empty")
    elif len(total_class) == 0 and len(class_attend) == 0:
        lines()
        print("User input --> Number of class attended field is empty")
        print("User input --> Total classes field is empty")

# User input is not empty
# Check for non-numeric input
# Calculate attendance percentage if inputs are valid
# Display result with eligibility messages
elif len(total_class) > 0 and len(class_attend) > 0:
    if not total_class.isdigit() or not class_attend.isdigit():
        if total_class.isdigit() and not class_attend.isdigit():
            lines()
            print("Class attended field must contain only numeric values")
        elif not total_class.isdigit() and class_attend.isdigit():
            lines()
            print("Total classes field must contain only numeric values")
        elif not total_class.isdigit() and not class_attend.isdigit():
            lines()
            print("Class attended field must contain only numeric values")
            print("Total classes field must contain only numeric values")

    elif total_class.isdigit() and class_attend.isdigit():
        total_class = int(total_class)
        class_attend = int(class_attend)

        attendance_percentage = (class_attend / total_class) * 100

        if attendance_percentage >= 75:
            lines()
            print(f"Total number of classes --> {total_class}")
            print(f"Classes attended -->--> {class_attend}")
            print(f"Attendance percentage --> {attendance_percentage:.2f}")
            print(f"You are eligible for write the exam")

        elif attendance_percentage > 60 and attendance_percentage <= 74:
            lines()
            print(f"Total number of classes --> {total_class}")
            print(f"Classes attended -->--> {class_attend}")
            print(f"Attendance percentage --> {attendance_percentage:.2f}")
            print(f"Attendance percentage is low. Please improve.")

        elif attendance_percentage <=59:
            lines()
            print(f"Total number of classes --> {total_class}")
            print(f"Classes attended --> --> {class_attend}")
            print(f"Attendance percentage --> {attendance_percentage:.2f}")
            print(f"Please contact the principal.")
