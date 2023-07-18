num = int(input("\n\t Enter any number = "))

i = 0; a = 0; b = 1

while a <= num:
    sum = a+b
    print("\n ",a)
    a = b
    b = sum
    i += 1
