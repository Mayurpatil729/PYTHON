import cmath
a = int(input("Enter first number (a!=0): "))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

d = (b**2)-(4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("The roots are", root1, "and", root2)
