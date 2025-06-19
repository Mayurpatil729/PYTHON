
# 1. Global Variables
# The variables which are declared outside of function are called global variables.
# These variables can be accessed in all functions of that module.

a = 10  # global variable


def f1():
    print(a)


def f2():
    print(a)


f1()
f2()


# 2. Local Variables:
# The variables which are declared inside a function are called local variables.
# Local variables are available only for the function in which we declared it.i.e from outside
# of function we cannot access.

def f1():
    a = 10
    print(a)  # valid


print()


def f2():
    print()
    # print(a) #invalid


f1()
f2()


# global keyword:
# We can use global keyword for the following 2 purposes:
# 1. To declare global variable inside function
# 2. To make global variable available to the function so that we can perform required
# modifications

a = 10


def f1():
    global a
    a = 729
    print(a)


def f2():
    print(a)


f1()
f2()

# Note: If global variable and local variable having the same name then we can access
# global variable inside a function as follows
print()
a = 10  # global variable


def f1():
    a = 729  # local variable
    print(a)
    print(globals()['a'])


f1()
