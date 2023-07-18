'''                  operators                     '''

'''                  Arithmetic                    '''

import math as m
from math import *           # *== for all
import math
a = 10
b = 20
print("a+b = ", a+b)
print("a-b = ", a-b)
print("a*b = ", a*b)
print("a/b = ", a/b)
print("a mod b = ", a % b)
print("a//b = ", a//b)   # floor division
print("a ** b = ", a**b)   # exponentition


'''                  Relational                     '''

print('\n\t The relational operator')

a = 10
b = 20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

print(10 < 20 < 30 < 40)
print(10 < 20 < 30 < 40 > 50)

print('\n\t The Equality operator')

print(10 == 20)

print(10 != 20)

print(10 == True)

print(False == False)

print("hello" == "hello")


print('\n\t The Logical operator')

# and ==> if both true then true
# or ==> if both false then false

print(True and False)

print(False and False)

print(True and True)

print(True or False)

print(True or True)


print(not False)


print('\n\t The X AND Y operator')

print(10 or 20)                            # or

print(0 or 20)

print(False or 20)


print(10 and 20)                          # and

print(0 and 20)

print(False and 20)

print(not 10)                     # not , complement

print(not 0)

'''                  Bitwise operator                      '''


print('\n\t The Bitwise operator')

print(10 << 5)
print(10 >> 5)
print(10 & 5)
print(10 | 5)
print(10 ^ 5)
print(~1)


'''                  Assignment operator                      '''


x = 20
x += 20
print(x)

# There is no  increment operator in python


'''                  TERNARY  operator                      '''

'''a = int(input("Enter the first number :"))
b = int(input("Enter the Second number :"))
c = int(input("Enter the Second number :"))

min = a if a < b else b
max = a if a > b and a > c else b if b > c else c

print("minimum value :", min)
print("maximun value :", max)   '''


'''                  SPECIAL  operator                      '''

print("\n\t\t Special operator")
a = 10
b = 20
print(a is b)           # address comparision
print(a is not b)


'''                  MEMBERSHIP  operator                      '''

print("\n\t\t Membership operator")
x = "hello world"

print('h' in x)

print('m' in x)

print('m' not in x)


print('h' not in x)

list = [10, 20, 30]

print(60 in list)


'''     Math module                    '''

print("\n\t Math module")

print(math.sqrt(16))
print(math.pi)


print(m.sqrt(729))
print(m.pi)                # math cant use


print(sqrt(729))
print(pi)


r = int(input("Enter the radius "))

area = pi*r**2

print("The area of circle : ", area)
