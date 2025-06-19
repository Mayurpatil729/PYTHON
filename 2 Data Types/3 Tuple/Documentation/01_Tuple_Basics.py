'''                        TUPLE DATA TYPE                                  '''

"""
1] insertion order preserved
2]  duplicate objects are allowed
3] heterogeneous objects are allowed
#* 4] List objects are immutable.i.e we can change the content
5] rounc brackets are not compulsory
"""

#!  creation of tuple objects :

t = ()
print(tuple)
print(type(t))


print()
A = 10, 203, 50
print(type(A))

#####################################################################


# immutable
my_tuple=(56,87,74,42,52)

# print(my_tuple)
# print(type(my_tuple))

# x=my_tuple.count(87)
# x=my_tuple.index(87)
# print(x)

# for i in my_tuple:
#     print(i)

my_list=list(my_tuple)
my_list.append(100)

my_tuple=tuple(my_list)
print(my_tuple)

my_string="code and debug"
#By index, By value

for index in range(0,len(my_string)):
    print(my_string[index])
    

for i in my_string:
    print(i)


for i in range(len(my_string)-1,-1,-1):
    print(i)


for ch in my_string:
    print(ch)
    
    
    

############################################










