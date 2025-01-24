# rows = i
# columns = j

# 5 stars rows and columns
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()


# 1 to 5 numbers.
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
        j = j + 1
    print()

# 5 to 1 numbers.
for i in range(1, 6):
    for j in range(5, 0, -1):
        print(j, end=" ")
        j = j - 1
    print()

for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(1, 6):
        print(i, end=" ")
    print()
