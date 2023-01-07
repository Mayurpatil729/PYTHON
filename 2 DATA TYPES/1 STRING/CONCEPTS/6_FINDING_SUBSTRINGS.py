# forward direction
# find()        and  index()

a = "Learning python is very easy"

print(a.find("python"))
print(a.find("very"))
print(a.find("java"))  # if not available then -1
print(a.find("r"))
print(a.rfind("r"))

print(a.index("python"))
print(a.index("very"))
# print(a.index("java")) # if substring not available then we will get error
print(a.index("r"))


# backward direction


a = "all is well"

print(a.rfind("s"))
print(a.rindex("s"))

s = input("Enter main string:")
subs = input("Enter sub string:")
try:
    n = s.index(subs)
except ValueError:
    print("substring not found")
else:
    print("substring found")


s = input("Enter main string:")
subs = input("Enter sub string:")
flag = False
pos = -1
n = len(s)
while True:
    pos = s.find(subs, pos+1, n)
    if pos == -1:
        break
print("Found at position", pos)
flag = True
if flag == False:
    print("Not Found")
