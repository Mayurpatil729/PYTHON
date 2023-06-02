x = eval(input('Enter first number :'))
y = eval(input('Enter second number :'))

choice = input(
    "Please Enter your choice: \nA for Addition, \nS for Subtraction, \nM for Multiplication and \nD for Division\n")


if choice == 'A':
    print('addition =', x+y)
elif choice == 'D':
    print('division =', x/y)
elif choice == 'M':
    print('multiplication =', x*y)
elif choice == 'S':
    print('subtraction =', x-y)
else:
    print('invalid input ')
