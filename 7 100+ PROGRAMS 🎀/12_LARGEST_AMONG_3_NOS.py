a = int(input("Enter first number : "))
b = int(input("Enter second number :"))
c= int(input("Enter third number :"))

max = a if a > b and a > c else b if b > c else c
print("Maximum Value:", max)
