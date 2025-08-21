#attendance checker

total_classes=int(input("Enter the total number of classes held\n"))
attended=int(input("Enter the number of classes attended\n"))

#calculate in percentage the number of classes attended out of total held 

attendance=(attended/total_classes)*100
attendance=float(attendance)

#condition to check whether the user can appear for exam or not
if attendance >=75:
    print(f"Total number of classes held {total_classes}")
    print(f"Number of classes attended {attended:2f}")
    print(f"Percentage --> {attendance}")
    print("Attendance is good and eligible to appear for exam")
elif attendance >=65 and attended < 75:
    print(f"Total number of classes held {total_classes}")
    print(f"Number of classes attended {attended:.2f}")
    print(f"Percentage --> {attendance}")
    print("Attendance is not great but can appear for exam with respect to principal permission")
else:
    print(f"Total number of classes held {total_classes}")
    print(f"Number of classes attended {attended}")
    print(f"Percentage --> {attendance:.2f}")
    print("Bad attendance, Sorry cannot appear for the exam.")
    print("Contact Principal")
