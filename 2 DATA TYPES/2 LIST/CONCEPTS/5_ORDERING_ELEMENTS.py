'''                 ORDERING ELEMENTS OF LIST                   '''

#! reverse():

n = [10, 20, 30, 40, 50, 60, 70, 80]
n.reverse()
print(n)


#! sort():
# For numbers == >default natural sorting order is Ascending Order
# For Strings == > default natural sorting order is Alphabetical Order
print()
n = [10, 2, 30, 4, 9, 62, 70, 80]
n.sort()
print(n)

print()
s = ["Dog", "Banana", "Cat", "Apple"]
s.sort()
print(s)

print()
n = [10, 2, 30, 4, 9, 62, 70, 80]
n.sort()
print(n)
n.sort(reverse=True)
print(n)
n.sort(reverse=False)
print(n)
