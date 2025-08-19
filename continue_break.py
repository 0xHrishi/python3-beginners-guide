#As the user to input two numbers and a stop number
#for loop and if the stop number is found, loop stop and break the iteration else continue until the number is found
first_number=int(input("Enter the first number\n"))
second_number=int(input("Enter the second number\n"))
stop_number=int(input("Enter the stop number\n"))

for number in range(first_number, second_number+1):
    if number == stop_number:
        print(f"Number is found --> {number}")
        print("Lets break")
        break
    else:
        print(f"Number is --> {number}")
        number+=1
        continue
