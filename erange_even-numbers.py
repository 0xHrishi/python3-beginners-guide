#script is to check whether the user would like to display even or odd numbers 

first_number=int(input("Enter the first number\n"))
second_number=int(input("Enter the second number\n"))

choice=input("Would like to print even or odd numbers\n").lower()

#Display even numbers
if choice == "even":
    for even_numbers in range(first_number, second_number+1):
        if even_numbers%2==0:
            print(f"Even numbers --> {even_numbers}")
        else:
            continue

#Display even numbers
elif choice == "odd":
    for odd_numbers in range(first_number, second_number+1):
        if odd_numbers%2!=0:
            print(f"Odd numbers --> {odd_numbers}")
        else:
            continue
else:
    print("Invalid user input")
