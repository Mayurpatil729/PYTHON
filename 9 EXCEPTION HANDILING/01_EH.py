try:
    x=int(input("Enter first number : "))
    y=int(input("Enter Second Number : "))
    print("The Result : ",x/y)

except BaseException as e:
    print("Exception Type : ",type(e))
    print("Exception Type : ",e.__class__)
    print("Exception Type : ",e.__class__.__name__)
    print("Exception Type : ",e)














