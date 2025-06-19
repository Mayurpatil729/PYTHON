'''             Aliasing and cloning of list objects             '''
#! The process of giving another reference variable to the existing list is called aliasing.

x=[10,20,30,40,50,60]
y=x
y[1]=88
print(x)
print(id(x))
print(id(y))


#! The process of creating exactly duplicate independent object is called cloning.
# = operator meant for aliasing
# copy() function meant for cloning
print()
x=[10,20,30,40,50,60]
y=x[:]
y[1]=88
print(x)
print(y)



#! 2 ] by using copy() function
print()
x=[10,20,30,40,50,60,70]
y=x.copy()
y[1]=69
print(x)
print(y)


