'''                               SET DATA STRUCTURE                         '''

#! Duplicates are not allowed.
#! Insertion order is not preserved.But we can sort the elements.
#! Indexing and slicing not allowed for the set.
#! Heterogeneous elements are allowed.
#! Set objects are mutable


"""            CREATION OF SET               """

s = {10, 20, 30, 40}
print(s)
print(type(s))

#! 1] using set function:
print()
l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
s = set(l)
print(s)

print()
s = set(range(5))
print(s)

print()
s = {}
print(s)
print(type(s))


#! 2]
