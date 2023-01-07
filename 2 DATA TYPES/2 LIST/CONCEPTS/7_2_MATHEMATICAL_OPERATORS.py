'''           Membership operators:                          '''

n=[10,20,30,40,50,60,70]
print(10 in n)
print(10 not in n)
print(50 in n)
print(50 not in n)



'''           List Comprehensions:             '''
print()
s=[x*x for x in range(1,11)]
print(s)
v=[2**x for x in range(1,6)]
print(v)
m=[x for x in s if x%2==0]
print(m)


print()
words= ["Balaiah","Nag","Venkatesh","Chiranjeevi"]
l=[w[0] for w in words]
print(l)


print()
fruits=["apple","banana","kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)