"""          LIST DATA TYPE  """

"""
1] insertion order preserved
2] duplicate objects are allowed
3] heterogeneous objects are allowed
4] List objects are mutable.i.e we can change the content
"""


# # !  creation of list objects :

# list=[]
# print(list)
# print(type(list))

# # output:
# # []
# # <class 'list'>

# #* with dynamic input

# l=eval(input('Enter the list : '))
# print(l)
# print(type(l))

# * with list() function  or constructor :

l = list(range(0, 10, 2))  # note double round brackets
print(l)
print(type(l))

m = "python"
l = list(m)
print(l)

# * with split() function :

s = "learning python is very very easy !!! "
l = s.split()
print(l)
print(type(l))


data = [1, 2, 3, 4, "mayur", "code"]
print(data)
print(*data)




