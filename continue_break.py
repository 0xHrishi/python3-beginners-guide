first=0

#If the number is equal to 6, the loop stop executing and exit the loop with the help of break statement otherwise continue
while first <=10:
    first+=1
    if first == 6:
        print("Number 6 is found")
        print("Lets break")
        break
    else:
        print(f"Number is --> {first}")
        continue
