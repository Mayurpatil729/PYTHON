'''                Mathematical operators                                '''

# concatenation (+)
print()
a = [10, 20, 30, 40, 50]
b = [60, 70, 80, 90, 100]
c = a+b
print(c)

# Repetition (*)
print()
x = [10, 20, 30]
y = x*3
print(y)

# comaparing list objects
print()
x = ["Dog", "Cat", "Rat"]
y = ["Dog", "Cat", "Rat"]
z = ["DOG", "CAT", "RAT"]
print(x == y)
print(x == z)
print(x != z)

print()
x = [50, 20, 30]
y = [40, 50, 60, 100, 200]
print(x > y)  # True
print(x >= y)  # True
print(x < y)  # False
print(x <= y)  # False

print()
x = ["Dog", "Cat", "Rat"]
y = ["Rat", "Cat", "Dog"]
print(x > y)  # False
print(x >= y)  # False
print(x < y)  # True
print(x <= y)  # True
