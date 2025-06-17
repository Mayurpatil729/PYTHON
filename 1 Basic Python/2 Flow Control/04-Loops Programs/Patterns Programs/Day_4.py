# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#         j=j+1
#     print()


# for i in range(1,6):
#     for j in range(5,0,-1):
#         print(j,end=" ")
#         # j=j-1
#     print()



# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print() 
    
    
# for i in range(5,0,-1):
#     for j in range(1,6):
#         print(i,end=" ")
#     print() 


# for i in range(1,6):
#     print(i*"* ",end=" ")
#     print()
# for i in range(6,0,-1):
#     print(i*"* ",end="")
#     print()

    
# n = 5
# for i in range(1, n+1):
#     print(" " * (n - i) + "* " * i)
    
    
    
# Diamond
# n=6
# for i in range(0,n+1):
#     print(" "*(n-i)+"* "*i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"* "*i)

# Main Line
# print("" * (n - i) + "* " * i)


# Hollow Squares 
# n = 5  # size of the square
# for i in range(1, n + 1):        # outer loop (rows)
#     for j in range(1, n + 1):    # inner loop (columns)
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()  # move to the next row



# n = 5
# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()
# A
# A B
# A B C
# A B C D
# A B C D E


# n = 5
# for i in range(n):
#     for j in range(i, -1, -1):
#         print(chr(65 + j), end=" ")
#     print()

