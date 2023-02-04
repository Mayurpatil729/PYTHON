a = eval(input("Enter the first tuple variable :"))
b = eval(input("Enter the second tuple variable :"))
print("before swapping:")
print("a=", a, "b=", b)
a, b = b, a
print("after swapping  ")
print("a=", a, "b=", b)