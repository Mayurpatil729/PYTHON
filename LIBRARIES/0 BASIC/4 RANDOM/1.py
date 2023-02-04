'''                               RANDOM MODULE                                           '''
# this module defines several functions to generate random numbers.
# We can use these functions while developing games, in cryptography and to generate
# random numbers on fly for authentication.


# random() == = > in between 0 and 1 (not inclusive)
# randint(x, y) == > in between x and y(inclusive)
# uniform(x, y) == > in between x and y(not inclusive)
#! 1 ] random() function:

# 0<i<1
from random import *
print()
print("This is random function")
for i in range(10):
    print(random())


#! 2 ] randint() function:

# 1<i<n
print()
print("This is randint function")
for i in range(10):
    print(randint(1, 100))


#! 3 ] uniform() function:
# It returns random float values between 2 given numbers(not inclusive)
print()
print("This is uniform function")
for i in range(10):
    print(uniform(1, 10))


#! 4 ] randrange([start],stop,[step]):

# eturns a random number from range
# start <= x < stop
# start argument is optional and default value is 0
# step argument is optional and default value is 1
# randrange(10)-->generates a number from 0 to 9
# randrange(1, 11)-->generates a number from 1 to 10
# randrange(1, 11, 2)-->generates a number from 1, 3, 5, 7, 9
print()
for i in range(10):
    print(randrange(1, 11, 2))


#! 5 ] choice() function:

# It wont return random number.
# It will return a random object from the given list or tuple.
print()
list = ["Sunny", "Bunny", "Chinny", "Vinny", "pinny"]
for i in range(10):
    print(choice(list))


print(choice("python"))


# write a python program as to genrate 6 digt number as otp
print()
for i in range(1):
    print("your otp is : ", randrange(100000, 1000000))


print()
for i in range(1):
    print("your otp is : ", randint(00000, 999999))

print()
for i in range(10):
    print("your otps are : ", randint(0, 9)*6, sep="")


# write a python program to generate password whenre 1,3,5=alphabets and 2,4,6= numbers

print()
for i in range(10):
    print(chr(randrange(65, 65+25)), randint(0, 9), chr(randrange(65, 65+25)), randint(0,
          9), chr(randrange(65, 65+25)), randint(0, 9), chr(randrange(65, 65+25)), sep="")
