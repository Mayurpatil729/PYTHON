x = eval(input('enter the year '))

if x % 4 == 0 or x % 100 == 0:
    print(x, ' year is leap year')
else:
    print(x, 'year is not leap year')