'''            DICIONARY DATA STRUCTURE                             '''

#! If we want to represent a group of objects as key-value pairs then we should go for Dictionary.

#! Duplicate keys are not allowed but values can be duplicated.
#! Hetrogeneous objects are allowed for both key and values.
#! insertion order is not preserved
#! Dictionaries are mutable
#! Dictionaries are dynamic
#! indexing and slicing concepts are not applicable
#! d[key]=value

#! CREATION OF DICTINARY
print()
d = {}
print(d)
print(type(d))

print()
d[100] = "python"  # * key should be always differents ,value should be same
d[101] = "c++"
d[102] = "java"
print(d)

#! ACCESSING THE DATA FROM THE DICTIONARYJ
print()
d = {100: "python", 200: "java", 300: "c++"}
print(d[100])
print(d[200])
print(d[300])
# print(d[400]) keyerror


#! UPDATE DICTIONARIES

print()
d = {100: "python", 200: "java", 300: "c++"}
print(d)
d[100] = "c"
d[200] = "R"
d[300] = "sql"
print(d)

#! DELETE ELEMENTS FROM DICTIONARY
# * del
m = {100: "python", 200: "java", 300: "c++"}
print(m)
del m[100]
print(m)
del m[200]
print(m)

# * d.clear()
print()
m = {100: "python", 200: "java", 300: "c++"}
print(m)
m.clear()
print(m)

# * del d : To delete total dictionary
print()
m = {100: "python", 200: "java", 300: "c++"}
print(m)
del m
# print(m) #m is not defined
