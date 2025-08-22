set={10,20,30}

print(set)
print(type(set))

#Frozen set
#Frozen sets are immutable i.e. user cannot add or modify values

set_1=frozenset({"a", "b"})
print(set_1)
print(type(set_1))


#Add new values
set.add(40)
print(set)

#remove
set.remove(40)
print(set)

#Clear sets
set.clear()
print(set)

#subset
set_1={1,2,4,5,6,7,8,9}
set_2={1,2,3}

if set_2.issubset(set_1):
    print("ok")
else:
    print("not ok")

#superset
if set_1.issuperset(set_2):
    print("ok")
else:
    print("not ok")
