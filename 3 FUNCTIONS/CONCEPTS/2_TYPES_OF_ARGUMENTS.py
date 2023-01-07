'''       Types of arguments             '''


# 1) positional arguments
print()


def sub(a, b):
    print(a-b)


sub(200, 100)
sub(30, 60)

# 2) keyword arguments  i.e by parameter name
print()


def wish(name, msg):
    print("hello", name, msg)


wish(msg="Good morning", name="mayur")  # ORDER OF ARGUMENT IS NOT IMPORTANT
wish(name="nikhil", msg="Good morning")
# wish(name="mayur","Good morning") invalid


# 3) Default arguments
print()


def wish(name="Guest"):
    print("hello", name, "Good morning")


wish("mayur")
wish()

# After default arguments we should not take non default arguments

# 4) VARIABLE LENGTH ARGUMENTS
print()


def sum(*n):
    total = 0
    for n1 in n:
        total = total+n1
    print("The sum= ", total)


sum()
sum(10)
sum(10, 20)
sum(10, 20, 30, 40)

print()


def f1(n1, *s):
    print(n1)
    for s1 in s:
        print(s1)


f1(10)
f1(10, 20, 30, 40)
f1(10, 'a', 20, 'b')
# Note: After variable length argument, if we are taking any other arguments then we
# should provide values as keyword arguments.


print()


def display(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)


display(n1=10, n2=20, n3=30)
display(rno=100, name="mayur", marks=80, subject="Python")
