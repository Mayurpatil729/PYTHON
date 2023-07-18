print("\nBefore swaping values are: ")
fno = int(input("\nEnter the first number : "))
sno = int(input("\nEnter the second number : "))

# without using third variable
fno, sno = sno, fno

# without using third variable
# fno=fno+sno
# sno=fno-sno
# fno=fno-sno

# with using temp variable
# temp = fno
# fno = sno
# sno = temp

print("\n After swaping the values are : ")
print("\nThe first number is : ", fno)
print("\nThe second number is : ", sno)
