'''                                 SLICE OPERATOR               '''

print("\n\t\t\t\tslice operator")

s = "Mayur"

print(s[1])

print(s[2])

print(s[3])

print(s[4])


print(s[-1])

print(s[-2])

print(s[-3])

print(s[-4])

print(s[-5])


'''                        slicing                       '''
print("\n\t\t\t\t\tslicing ")

s = "Mayur patil"  # s [ begin : end -1 : step ]

print(s[1:4])

print(s[2:4])

print(s[4:])

print(s[1:])


print(s[1:3])

print(s[-1:-3])             # negative not allowed


print(s[1:10:3])


'''              slicing           '''


print(s*3)
print(s*5)

print("\n\t\tTo calculate length")

print(len(s))


'''          TYPE CASTING     '''

print("\n\n For TYPE CASTING")

int(True)

print(int)
# print(True)



print("\nobject creation ");
m = "mayur"
v = "mayur"
x = "mayur"
print(id(m))
print(id(v))
print(id(x))

n=257
p=257

print(n is p)
print(id(n))
print(id(p))