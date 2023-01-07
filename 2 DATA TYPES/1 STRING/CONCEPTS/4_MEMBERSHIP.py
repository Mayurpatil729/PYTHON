# Membership operator  :is , in
s = input("Enter main string :")
subs = input("Enter the substring :")

if subs in s:
    print(subs, "is found in main string")
else:
    print(subs, "is not found in main string")


z = "membership"
print('m' in z)
print('z' in z)
# == is used to check content comparision
# is  is used to check reference comparision


list1 = ["A", "B", "C"]
list2 = ["A", "B", "C"]
print(id(list1))
print(id(list2))
print(list1 is list2)



# comaparision operator
s1 = input("Enter first string:")
s2 = input("Enter Second string:")
if s1 == s2:
    print("Both strings are equal")
elif s1 < s2:
    print("First String is less than Second String")
else:
    print("First String is greater than Second String")


