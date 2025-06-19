'''        MANIPULATING ELEMENTS OF LIST               '''

#! 1 ] append()

list = []
list.append("a")
list.append("b")
list.append("c")
list.append("d")
list.append("e")
print(list)

list=[] 
for i in range(101): 
    if i%10==0: 
        list.append(i) 

print(list)

#! 2 ] insert()
print()
n1 = [1, 2, 3, 4, 5, 6, 7]
n1.insert(1, 888)
n1.insert(2, 999)  # index wise
n1.insert(10000, 999)  # index wise
n1.insert(-10000, 999)  # if smaller than min then at first position
print(n1)


#! 3 ] extend() : to join two lists
print()
n1 = ['a', 'b', 'c']
n2 = ['d', 'e', 'f']
n1.extend(n2)  # or n3=n1+n2
print(n1)
n2.extend('x')
print(n2)

#! 4 ] remove()
print()
n = [10, 20, 30, 40, 50]
n.remove(40)
print(n)
# n.remove(70)  # value error

#! 5 ] pop()  : this is the only function which returns
print()
n = [10, 20, 30, 40, 50]
print(n.pop())  # default at from last
print(n.pop(0))  # index wise
print(n)

#! 6 ] clear function : clear the list elements
print()
n = [1, 2, 3, 4, 5, 6, 7]
n.clear()
print(n)


#! 7 ] del keyword  : to delete items, and also to delete the list completely
print()
n3 = [1, 2, 3, 4, 5, 6, 7]
del n3[1]
print(n3)
del n3
print(n3)

# map function

ls = list(map(int, input.split()))
