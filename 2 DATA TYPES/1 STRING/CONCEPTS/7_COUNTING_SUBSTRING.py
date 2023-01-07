m = "abcabcaabaabcaadsa"

print(m.count('a'))
print(m.count('b'))
print(m.count('c'))
print(m.count('a', 3, 9))  # 3 is begin and 9 is end-1


# REPLACING A STRING WITH ANOTHER STRING

m1 = "write once run anywhere"

# m.replace(oldstring,newstring)
m2 = m1.replace("once", "twice")
print(m1)
print(m2)

print(m1.replace("once","twice"))


s="abab"
s1=s.replace("a","b")
print(s,"is available at :",id(s))
print(s1,"is available at :",id(s1))