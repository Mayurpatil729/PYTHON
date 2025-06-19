'''                REPLACEMENT OPERATOR                            '''

name = "rohan"
salary = 100000
age = 32

print("{} salary is :{} and his age is :{} ".format(name, salary, age))

print("{1} salary is :{0} and his age is :{1} ".format(name, salary, age))

print("{x} salary is :{y} and his age is :{z} ".format(x=name, y=salary, z=age))


print() 
# f strings
letter = "hey my name is {} and i am from {} "
country = 'india'
name = 'rohan'

print(letter.format(name, country))
print(f"hey my name is {name} and i am from {country}")

print()
price = 49.09999
txt = f"For only {price:.2f} dollars "
print(txt.format(price))
print(type(f"{3*20}"))


name = input("Enter your name")
print(f'My name is {name}.')

x = eval(input('enter first number'))
y = eval(input('enter second number'))
if x > y:
    print(f'max={x}')
else:
    print(f'min={y}')


n = eval(input('enter the number'))
if n > 0:
    print(f'{n} is positive number')
if n < 0:
    print(f'{n} is negative number')
if n == 0:
    print(f'{n} is neutral')


# ENUMERATE FUNCTION
print()
marks = [12, 24, 36, 48, 60]
index = 0
for mark in marks:
    print(mark)
    if (index == 3):
        print("enumerate")
    index += 1

print()
marks = [12, 24, 36, 48, 60]
for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("enumerate")













