def fact(n):
    return 1 if (n == 1 or n == 0) else n*fact(n-1)


num = int(input('enter the number '))
print(f'factorial of {num} is {fact(num)}')
fact(num)