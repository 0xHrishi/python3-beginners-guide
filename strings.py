#This script focus on string, concatenation, formatted strings

#User enter his/her full name
full_name=input("Enter your full name\n")
#Enter age
age=input("Enter your age\n")

#string triple quotes to dislay larger text 
print("""Hi there,

Note: It's important to ensure that you have created a snapshot of the virtual machine before making any configuration changes. This will allow you to revert to a previous state if needed. Regular snapshots can save a great deal of time and frustration if something goes wrong.

If you have any further questions or need assistance, feel free to ask.
Please do not forget to rate the course and leave a review
Thanks and let's keep learning together """)
#Print function to display the user input
print(full_name, age)

#String concatenation
print("String Concatentation --> Your name is --> " + full_name + " and age is --> " + str(age))

#Formatted strings
print(f"Formatted strings --> Your name is --> {full_name} and age is --> {age}")
