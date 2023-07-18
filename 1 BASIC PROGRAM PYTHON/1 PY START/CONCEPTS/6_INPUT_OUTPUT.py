'''            Input output statements           '''


eno = int(input("\n\t Enter the Employee no ."))
ename = input("\n\t Enter Employee name :")
esal = float(input("\n\t Enter the salary :"))
eaddr = input("\n\t Enter the employee address : ")
married = bool(input("\n\t Employee married ? [True | False ]:"))

print("\n\t Please confirm information")
print("\n\t Employee no:", eno)
print("\n\t Employee name : ", ename)
print("\n\t Employee salary :", esal)
print("\n\t Employee address : ", eaddr)
print("\n\t Employee married :", married)


"""              addition of two numbers                """
print("\n\tProgram for addition of two numbers ")
a = int(input("\n\tEnter the first number:"))
b = int(input("\n\tEnter the second number :"))

print("\n\tthe Addition :", a+b)

print("\n\tthe subtraction:", int(input("Enter the first number:")) -
      int(input("Enter the second number :")))


"""                 split and eval                 """

print("\nProgram for multiplication of two numbers ")

#a,b=[int(x) for x in input("Enter the 2 numbers :").split()]
#a, b = [int(x) for x in input("Enter the 2 numbers :").split(",")]
a, b = [int(x) for x in input("Enter the 2 numbers :").split()]

print("\n\tproduct is :", a*b)


print("Eval Function")

m = eval("12+60+65+45+85")
print(m)

x = eval(input("Enter the Expression :"))
print(x)


"""               Output statements                 """

print("hello world")

print("hello \n world ")

print("hello \t world")

print("hello"+"world")  # string concatenation

print("world"*3)  # compulsory one should be of int type

print("hello", "world")            # space is default separator


# no. of arguments

a, b, c = 10, 30, 50

print("The values are :", a, b, c)


print(a, b, c, sep=',')
print(a, b, c, sep=':')

# end attribute

print("hello", end=' ')
print("world", end=' ')      # default value of end attribute is \n


# print    string, variable list

s1 = "java"
s2 = "python"

print("you are learning", s1, "and", s2)

# print(formatted string)

a = 10
b = 12

print("a value is %i and b value is %i " % (a, b))

m = 'mayur'
l = [52, 52, 39]

print("hello %s ... The list of items are %s " % (m, l))
# format specifier is allowed


# repalcement operator


name = "mayur"
sal = 52
print("hello {0} your salary is {1}".format(name, sal))

print("hello {x} your salary is {y}".format(x=name, y=sal))


print
