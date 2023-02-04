
#! 6 ] popitem() :

d = {100: "john ", 200: "don", 300: "harry"}
print(d)
print(d.popitem())
print(d)

#! 7 ] keys():
# it returns all keys associated with dictionary

print()
d = {100: "john ", 200: "don", 300: "harry"}
print(d.keys())
for k in d.keys():
    print(k)

#! 8 ] values():
# It returns all values associated with the dictionary
print()
d = {100: "john ", 200: "don", 300: "harry"}
print(d.values())
for v in d.values():
    print(v)

#! 9 ] items():

# it returns list of tuples representing key-value pairs.

print()
d = {100: "john", 200: "don", 300: "harry"}
for k, v in d.items():
    print(k, "--", v)


#! 10 ] copy():
print()
d = {100: "john", 200: "don", 300: "harry"}
d1 = d.copy()
print(d1)


#! 11 ] setdefault():

# d.setdefault(k, v)
# If the key is already available then this function returns the corresponding value.
# If the key is not available then the specified key-value will be added as new item to the
# dictionary.

print()
d = {100: "john", 200: "don", 300: "harry"}
print(d.setdefault(400, "pavan"))
print(d)
print(d.setdefault(100, "sachin"))
print(d)


#! 12 ] update():

# d.update(x)
# All items present in the dictionary x will be added to dictionary d

print()
d = {100: "john", 200: "don", 300: "harry"}
x = {400: "john", 500: "don", 600: "harry"}
d.update(x)
print(d)
