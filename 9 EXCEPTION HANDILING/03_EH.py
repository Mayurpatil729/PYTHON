try:
    x=int(input("Enter first number : "))
    y=int(input("Enter Second Number : "))
    print(x/y)
except ZeroDivisionError:
    print("ZeroDivisionError : cannot divide with zero")
except:
    print("Default Except : please provide valid input only ")
    
    
    
    
    
    