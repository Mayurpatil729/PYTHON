'''            int        '''

print("\n\t\tint data type")

print(int(19))
print(int(1912.5))
print(int(1912.5))
print(int(True))
# print(int("mayur"))
# print(int(10+5j))


'''            float       '''

print("\n\t\tfloat data type")

print(float(2.9))
print(float(2))
print(float(True))
# print(float(10+6j))
# print(float("mayur"))


'''            complex       '''

print("\n\t\tComplex data type")

print(complex(10))
print(complex(10+4j))
print(complex(10+5.3j))
print(complex("10"))  # print(complex("mayur"))
print(complex(10))

'''            Bool      '''

print("\n\t\tBool data type")

print(bool(10))
print(bool(0))
print(bool("mayur"))
print(bool(10+4j))
print(bool(10.6))
print(bool())


'''           str      '''

print("\n\t\tstr data type")

print(str("10"))
print(str("mayur"))
print(str("1.3"))
print(str("10+5j"))
print(str("True"))

'''           bytes data type   '''

print("\n\t\tbytes data type")

x = [10, 20, 30, 40, 50]

b = bytes(x)

print(type(b))
print(b[0])
print(x)

# range 0 to 256

'''           byteaarray data type   '''

print("\n\t\tbytearray data type")

m = [1, 0, 20, 30, 40, 50]

b = bytearray(m)
print(type(b))
m[0] = 23
print(m[0])  # mutable
print(b[0])
print(m)


# range 0 to 256

'''           list  data  type   '''

print("\n\t\t list data type")

# mutable,slicing allowed,insertion ordered iś preserved
list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]

print(list)

list.append("mayur")
print(list)

list.remove(77)
print(list)

print(list[-3])

'''          tuple  data  type   '''

print("\n\t\ttuple data type")

t = (12, 13, 14, 15, 16, 17, 181, 95)

print(t)

print(t[0])

print(type(t))  # immutable


'''         range  data  type   '''

print("\n\t\trange data type")

print(range(10))

r = range(10)
for i in r:
    print(i)                   # generate numbers

t = range(10, 30)
for j in t:
    print(j)

t = range(30, 50, 5)
for j in t:
    print(j)


'''         set  data  type         '''

print("\n\t\tSet data type")

s = {"mango", "lemon", "coconut", "watermelon", "pineapple"}

print(s)


print(type(s))            # does not support indexing
# mutable


s.add("beetroot")
s.remove("lemon")

print(s)


'''         frozenset  data  type   '''

print("\n\t\tfrozenset data type")


p = {"mango", "lemon", "coconut", "watermelon", "pineapple"}

fs = frozenset(p)

print(type(p))
print(type(fs))
print(p)
# does not support indexing
# immutable


'''        Dict   data  type   '''


print("\n\t\tdict data type")


m = {101: "hello", 102: "world", 103: "shiva"}

print(m)  # mutable
print(m[102])                 # keys cant be duplicate, values can duplicate

m[101] = 'python'

print(m)

m = {}                     # dictionary
print(m)


'''        None   data  type   '''

print("\n\t\tNone data type")


def m1():
    a = 10
    print(m1)
    None


"""            The end                      """
