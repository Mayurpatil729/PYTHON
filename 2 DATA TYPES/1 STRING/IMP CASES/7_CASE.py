# formatting dictionary members using format()


person={'age':20,'name':'john'}
print("{p[name]}'s age is : {p[age]}".format(p=person))

#p is alias name of dictionary

print()
person = {'age': 48, 'name': 'john'}
print("{name}'s age is: {age}".format(**person))













