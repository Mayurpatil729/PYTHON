
#!                     BASIC PROGRAM FOR INT,FLOAT,COMPLEX,BOOL,STR 


# Simple print

print("\t\t\t\t\tWELCOME TO PYTHON , MAYUR ")

a = 729
print("\n\tvalue of a = ", a)


"""                                   INT DATA TYPE                                               """


# Decimal conversion                 [BASE 10 ==0 TO 9]
print(" \t\t\t\t\t DECIMAL CONVERSION")
a = 1111
print("\n\tvalue of a = ", a)


# Binary conversion                  [BASE 2 ==0 TO 9]
print(" \t\t\t\t\t BINARY CONVERSION")
a = 0b1111
print("\n\tvalue of a = ", a)

a = 0B1111
print("\n\tvalue of a = ", a)

a = -0b1111
print("\n\tvalue of a = ", a)


# Octal coversion                    [BASE 8 ==0 TO 7]
print(" \t\t\t\t\t OCTAL CONVERSION")
a = 0o1234
print("\n\tvalue of a = ", a)

a = 0O1234
print("\n\tvalue of a = ", a)

# a=-0b1234
print("\n\tvalue of a = ", a)


# Hexadecimal coversion              [BASE 16 ==0 TO 9 ,A TO F, a TO f]
print(" \t\t\t\t\t HEXADECIMAL CONVERSION")
a = 0x1234
print("\n\tvalue of a = ", a)

a = 0X1234
print("\n\tvalue of a = ", a)

a = -0x1234
print("\n\tvalue of a = ", a)


'''                                      FLOAT                                                '''

print("\n\t\t\t\t\t\t\t FLOAT")

# ONLY IN DECIMAL FORM
f = 123.45
print("\n\t value of f =", f)


# EXPONENTION
f = 1.2e3
print("\n\t Value of f = ", f)


'''                                     COMPLEX                                                '''

print("\n\t\t\t\t\t\t\t  COMPLEX")

# a=real part
# b=imaginary part , j is compulsory

a = 10+20j
b = 30-2.3j

print(a)
print(b)

print("\n\t value of a+b = ", a+b)
print("\n\t value of a-b = ", a-b)
print("\n\t value of a*b = ", a*b)
print("\n\t value of a/b = ", a/b)


a.real
print("\n\t Value of real part = ", a.real)

a.imag
print(" \n\t Value of imaginary part =  ", a.imag)


'''                                       BOOL                                               '''
print("\n\t\t\t\t\t\t\t  BOOL")

a = True                               # 1
b = False                              # 0
print("\n\t\t\ta+b= ", a+b)           # 1+0

a = 20
b = 10

print(a > b)
print(a < b)
print(a*b)
print(a-b)
print(a >= b)


'''                                       STR                                                '''
print("\n\t\t\t\t\t\t\t  STR")

print('''this 
      is 
      awesome''')


m = "mayur patil"
print(m)


m = "cricket 'or' football"
print(m)


m = """cricket "or" football"""
print(m)








'''   
   
print(type(23))  # int
print(type(3.14))  # float
print(type("hello"))  # str

print(type("23"))  # str
print(type("3.24"))  # str

print(type(None))  # NoneType
print(type(True))  # bool
print(type(False))  # bool

print(type([]))  # list
print(type({}))  # dict
# print(type(hello))  # NameError: name 'hello' is not defined
print("Still running")



'''


 