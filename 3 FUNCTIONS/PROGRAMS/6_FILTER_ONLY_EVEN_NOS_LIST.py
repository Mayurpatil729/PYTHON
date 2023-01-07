
#! filter only even numbers from the list by using filter() function?
# * without lambda function:
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


l = [0, 5, 10, 15, 20, 25, 30, 35, 40]
l1 = list(filter(isEven, l))
print(l1)


# * with lambda function:
print()
l = [0, 5, 10, 15, 20, 25, 30, 35, 40]
l1 = list(filter(lambda x: x % 2 == 0, l))
print(l1)
l2 = list(filter(lambda x: x % 2 != 0, l))
print(l2)


# MAP FUNCITION

# without lambda
print()
l = [1, 2, 3, 4, 5]


def doubelt(x):
    return 2*x


l1 = list(map(doubelt, l))
print(l1)

# with lambda

l = [1, 2, 3, 4, 5]
l1 = list(map(lambda x: 2*x, l))
print(l1)


print()
l = [1, 2, 3, 4, 5]
l1 = list(map(lambda x: x*x, l))
print(l1)

print()
l1 = [1, 2, 3, 4]
l1 = [2, 3, 4, 5]
l3 = list(map(lambda x, y: x*y, l1, l2))
print(l3)
