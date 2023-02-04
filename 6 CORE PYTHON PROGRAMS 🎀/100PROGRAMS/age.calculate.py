age = eval(input('enter the age'))
if age<18:
    print('child')
elif age<65:
    print('adult')
elif age<120:
    print('senior citizen')
else:
    print('invalid input')