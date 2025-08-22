#deep copy example
#If a user copy list from the original list, any changes made the copy list will affect original list
#To avoid and have a separate independed copy, make an deep copy 

import copy

#list_2 same as list_1
list_1=[1,2,3]
list_2=list_1

#print list_1 and list_2
print(list_1)
print(list_2)

#confirm the data type
print(type(list_1))
print(type(list_2))

#Deep copy
#list_2 is an exact copy from the list_1 but an independent copy
#any changes made to list_2 will not affect list_1 

list_2=copy.deepcopy(list_1)
print(list_2)
list_2.append("Hrishi")

print(list_1)
print(list_2)
