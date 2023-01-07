'''                   Mathematical operations                                 '''

#! 1 ] union(): to return all elements present in both sets
print()
x = {10, 20, 30, 40}
y = {50, 60, 70, 80}
print(x.union(y))
print("or")
print(x | y)


#! 2 ] intersection(): Returns common elements present in both x and y
print()
x = {10, 20, 30, 40}
y = {30, 40, 70, 80}
print(x.intersection(y))
print(x & y)

#! 3] difference(): returns the elements present in x but not in y,
print()
x = {10, 20, 30, 40}
y = {30, 40, 70, 80}
print(x.difference(y))
print(x-y)
print(y-x)

#! 4] symmetric_difference():
print()
x = {10, 20, 30, 40}
y = {30, 40, 70, 80}
print(x.symmetric_difference(y))
print(x ^ y)


#! 5] Membership operators :
m = set("python")
print(m)
print('p' in m)
print('z' in m)


#! 6] SET COMPREHENSION :
s = {x*x for x in range(5)}
print(s)

r = {2**x for x in range(2, 10, 2)}
print(r)
