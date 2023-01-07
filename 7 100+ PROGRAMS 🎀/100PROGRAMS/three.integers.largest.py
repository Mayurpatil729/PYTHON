x = eval(input('enter first number'))
y = eval(input('enter second number'))
z = eval(input('enter third number'))
if x>y and x>z:
    print(x,"is largest number")
elif y>z:
    print(y,"is largest number")
else:
    print(z,"is largest number")