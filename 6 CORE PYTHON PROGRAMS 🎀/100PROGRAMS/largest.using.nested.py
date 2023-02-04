x = int(input('enter the number'))
y = int(input('enter the number'))
z = int(input('enter the number'))
if x>y:
    if x>z:
        m = x
    else:
        m = z
elif y>z:
    m = y
else:
    m = z

print('maximum=',m)