"""
Write a program that prompts the user to specify the length of a list and then requests numbers to populate that list. Display the final list as the output
"""

# length = int(input("Enter the length of the list : "))

# lst = []
# for i in range(0, length):
#     lst.append(input(f"Enter the number in position {i} : "))

# print("The List is : ", lst)


"""
Create a list and prompt the user for an 'old number' followed by a
'new number.' If the 'old number' exists in the list, replace it with the 'new
number' provided by the user.
"""
# my_list = [5, 10, 15, 20, 25]

# old = int(input("Enter the old Number : "))
# new = int(input("Enter the newew Number : "))

# for i in range(0, len(my_list)):
#     if my_list[i] == old:
#         my_list[i] = new

# print("The Updated list is : ", my_list)


# for i in range # position
# for i in list # value

#! **************************************************

"""
Remove all the even numbers from the list.
"""
# my_list = [22, 55, 33, 88, 66, 99, 66, 88]
# my_list = [45, 66, 66, 66, 78, 11, 11, 12, 12, 12]
# for i in range(len(my_list) - 1, -1, -1):
#     if my_list[i] % 2 == 0:
#         my_list.pop(i)

# print("The final list is : ", my_list)

# a = [45, 65, 12, 32, 99, 87]
# b = []
# for i in a:
#     if i % 2 != 0:
#         b.append(i)

# print(b)


#! **************************************************
"""
Ask the user for a number, Then, from a list of numbers, remove all
the numbers that can be divided by the number the user entered. (DO on
your own).
"""

# my_list = [10, 15, 20, 25, 35]
# num = int(input("Enter a number: "))

# for i in my_list[:]:  # Iterate over a copy
#     if i % num == 0:
#         my_list.remove(i)

# print("Updated list:", my_list)

# Solution: Iterate Over a Copy:
# By iterating over a copy (my_list[:]), the iteration is unaffected by modifications to the original list. The loop operates on the copy, while remove or pop changes the original.

# Use safe approaches like list comprehension, iterating over a copy, or reverse iteration.


""" 
Generate a list of at least IO numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list.
"""

# my_list = [3, 8, 17, 22, 30, 35, 41, 48, 50]
# odd = []
# even = []
# for i in my_list:
#     if i % 2 == 0:
#         even.append(i)
#     if i % 2 != 0:
#         odd.append(i)


# print("The old list is : ", odd)
# print("The even list is : ", even)


# for i in my_list iterates over elements directly.
# for i in range(0, len(my_list)) iterates over indices, requiring you to access elements with my_list[i].
# for i in my_list: and check i directly.
# for i in range(0, len(my_list)): and use my_list[i].


#! **************************************************
""" 
Start by creating two separate lists with random numbers. Then, create a third list that merges the numbers from the first and second lists together.
"""
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# # result = []
# result = list1 + list2

# # for num in list1:
# #     result.append(num)

# # for num in list2:
# #     result.append(num)

# print(result)


#! **************************************************
