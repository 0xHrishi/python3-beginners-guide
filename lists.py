#Lists
#Lists --> Allows the user to store multiple values in a single variable
details=["Hrishi", "Dilip", "Ghosalkar", 30, 40, 50]

print(details)
print(type(details))

#list slicing
#[start:end:step value]
print(details[0])
print(details[0:5:2])

#popular lists methods
#append, append a value to the end of the list
details.append("Cyber security")
print(details)

#remove, remove the value as per the user specified value
details.remove("Cyber security")
print(details)
#pop, remove the value from the list based upon the index position
details.pop(0)
print(details)
#insert, insert a new value based upon the index
details.insert(0,"Hrishi")
print(details)

#list sporting
new_details=[5,6,1,2,3]
new_details.sort()
print(new_details)

#list reverse
new_details.reverse()
print(new_details)
