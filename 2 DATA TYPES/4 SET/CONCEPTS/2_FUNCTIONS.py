'''         FUNCTIONS                    '''

# * TO ADD ELEMENTS

#! 1] add(x): only add 1 elements
s = {10, 20, 30}
s.add(40)
print(s)

#! 2] update(x,y) :not add single elements ,add iterable objects,list,tuple

print()
s = {10, 20, 30, 40}
l = [90, 50, 88, 66, 77]
s.update(l, range(5))
print(s)


# 1. s.add(10)
# 2. s.add(10, 20, 30) TypeError: add() takes exactly one argument(3 given)
# 3. s.update(10) TypeError: 'int' object is not iterable
# 4. s.update(range(1, 10, 2), range(0, 10, 2))


# * TO REMOVE ELEMENTS

#! 1] pop(): removes and returns some random element from the set.
print()
s={4,5,9,6,8,3}
print(s)
print(s.pop())
print(s)

#! 2] remove(x): removes specified element,specified element not present in the Set then we will get KeyError

print()
s={40,90,80,60,30,70}
s.remove(40)
# s.remove(88) # key error
print(s)

#! 3] discard(x): removes the specified element,specified element not present in the set then we won't get any error.
print()
s={10,60,8,99,7,55,22}
s.discard(10)
print(s)
s.discard(100)
print(s)


#! 4] clear(): remove all elements from the set.
print()
s={10,20,30}
print(s)
s.clear()
print(s) # empty set