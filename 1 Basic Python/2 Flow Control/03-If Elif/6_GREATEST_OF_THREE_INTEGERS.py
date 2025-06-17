print("\n\t Program to check Three of two integers ")

n1 = int(input("\n\t Enter the fist number = "))
n2 = int(input("\n\t Enter the second number = "))
n3 = int(input("\n\t Enter the third number = "))

if n1 == n2 and n2 == n3:
    print("\n\t All numbers are same")
elif n1 > n2 and n1 > n3:
    print("\n\t %i ,first number is greater" % (n1))
elif n2 > n3:
    print("\n\t %d ,second number is greater" % n2)
else:
    print("\n\t %d ,third number is greater " % n3)


'''max=a if a>b and a>c else b if b>c else c 
 print("Maximum Value:",max) '''
