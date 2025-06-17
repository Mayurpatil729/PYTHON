
# try:
#     x=int(input("Enter First Number : "))
#     y=int(input("Enter Second Number : "))
#     print("The Result : ",x/y)
# except  ZeroDivisionError :
#     print("Cannot divide with zero")
# except ValueError:
#     print("Please provide int values only")

##########################################


try:
    print(10/0)
except ArithmeticError:
    print("Arithmetic Error")
except ZeroDivisionError:
    print("ZeroDivisionError")



# Top to Bottom







