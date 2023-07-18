# FIBONACCI SERIES

n = int(input("Enter any number : "))


a = 0
b = 1
c = 0
print("\n0")
for i in range(1, n):
    a = b
    b = c
    c = a+b
    print(" ", c)


# num = int(input('ENTER THE NUMBER : '))
# n1 = 0
# n2 = 1
# print("Fibonacci Series:", n1, n2,end=" " )
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")

# print()
