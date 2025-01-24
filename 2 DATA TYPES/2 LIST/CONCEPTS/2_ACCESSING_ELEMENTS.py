# ! ACCESSING ELEMENTS OF LIST :

# * 1] BY USING INDEX :

list = [10, 20, 30, 40, 50]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print()
print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
print()


# * 2 ] BY USING SLICE OPERATOR :

n = [1, 5, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])
print(n[4:100])
print()


# Iterate by position/index :
for i in range(0, len(n)):
    print(n[i])

print()
# iterate by value :
for i in n:
    print(i)
print()


# ? list is mutable

n = [10, 20, 30, 40, 50]
print(n)
n[2] = 99
print(n)


