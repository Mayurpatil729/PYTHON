# Make your own list. print the list in reverse.
# lst = [4, 35, -78, "code", 45, "Debug"]
# print(lst[::-1])
# print(*lst[::-1])
# # from len(lst) to 0
# for i in range(len(lst) - 1, -1, -1):
#     print(lst[i], end=" ")


# ! ******************************************************************

# Make your own list. Print all the even numbers from the list.
# lst = [2, 3, 4, 5, 6, 7, 55, 9, 10, 11, 12, 13, 14]
## iteration by Index
# for i in range(0, len(lst)):
#     if lst[i] % 2 == 0:
#         print(lst[i], end=" ")


# Iteration by value
# for j in lst:
#     if j%2==0:
#         print(j,end=" ")

# ! ******************************************************************


# Make your own list. Print all the even numbers from the list.
# lst = [2, 3, 4, 5, 6, 7, 55, 9, 10, 11, 12, 13, 14]
# # iteration by Index
# for i in range(0, len(lst)):
#     if lst[i] % 2 != 0:
#         print(lst[i], end=" ")

# ! ******************************************************************


# Make your own list.Print all the elements present at even index position.
# lst = [2, 3, "code", 454, "Debug"]
# # iteration by even Index
# for i in range(0, len(lst)):
#     if i % 2 == 0:
#         print(lst[i], end=" ")


# ! ******************************************************************

# Make your own list. Print the sum of all elements present in that list.
# lst = [51, 85, 91.66, 52, 44, 100, 200]
# sum = 0
# for i in range(0, len(lst)):
#     sum = sum + lst[i]

# print(sum)

# ! ******************************************************************


# Make your own list. Count the number of even numbers present in that list.
# lst=[51,85,91.66,52,44,100,200]
# # iteration by Index
# count=0
# for i in range(0, len(lst)):
#     if lst[i] % 2 == 0:
#         count=count+1

# print(count)

# ! ******************************************************************

# Make your own list. count how many numbers are divisibel by both 2 and 5
# lst = [51, 85, 91.66, 52, 44, 100, 200]
# # iteration by Index
# count = 0
# for i in range(0, len(lst)):
#     if lst[i] % 2 == 0 and lst[i] % 5 == 0:
#         count = count + 1

# print(count)

# ! ******************************************************************

# Make your own list. Print the sum of all even elements present in that list.
# lst = [51, 85, 1748, 52, 44, 100, 200]
# sum = 0
# for i in range(0, len(lst)):
#     if lst[i] % 2 == 0:
#         sum = sum + lst[i]

# print(sum)

# ! ******************************************************************
# Make your own list. sum of numbers are divisible by both 3 and 4
# lst = [51, 85, 1748, 52, 44, 100, 200]
# # iteration by Index
# sum = 0
# for i in range(0, len(lst)):
#     if lst[i] % 3 == 0 or lst[i] % 4 == 0:
#         sum = sum + lst[i]

# print(sum)


# ! ******************************************************************
# Make your own list. Print the largest number present in that list.

# lst = [51, 85, 1748, 52, 44, -10, 200]
# largest = lst[0]
# smallest = lst[0]
# for i in range(0, len(lst)):
#     if lst[i] > largest:
#         largest = lst[i]

# for i in range(0, len(lst)):
#     if lst[i] < smallest:
#         smallest = lst[i]

# print("Smallest Number : ",smallest)
# print("Largest Number : ",largest)


# ! ******************************************************************


# Make your own list.Print how many positive and negative numbers are here.
# f = [1,6,-3,-5,9,-1,33]

# Solution:
# pos = 0
# neg =0
# for i in f:
#     if i >= 0:
#         pos+= 1
#     else:
#         neg+= 1
# print(f"Positive numbers: {pos}")
# print(f"Negative numbers: {neg}")
# print("\n")