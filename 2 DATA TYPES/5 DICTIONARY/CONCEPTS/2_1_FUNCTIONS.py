'''          FUNCTIONS                  '''
#! 1 ] dict():
print()
d = dict({1: 'python', 2: 'c++', 3: 'java'})
print(d)
d = dict([(100, "python"), (200, "java"), (300, "c++")])

#! 2 ] len():
print()
d = dict({1: 'python', 2: 'c++', 3: 'java'})
print(len(d))

#! 3 ] clear():
d = dict({1: 'python', 2: 'c++', 3: 'java'})
print(d.clear())

#! 4 ] get():
print()
d = dict({1: 'python', 2: 'c++', 3: 'java'})
print(d)
print(d[1])
print(d[2])
print(d[3])
# print(d[5])  #keyerror
print()
print(d.get(1))
print(d.get(2))
print(d.get(1, "sql"))  # wont update
print(d.get(4, "sql"))  # new elements is added

#! 5 ] pop():
print()
d = {1: 'python', 2: 'c++', 3: 'java'}
print(d.pop(1))
print(d)
print(d.pop(2))
print(d)
print(d.pop(3))
print(d)


